#from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Count # annotate에서 Count 사용하기 위함

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *

def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)


class PostApiView(APIView):
    def get_objdect(self, pk):
        post = get_object_or_404(Post, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_objdect(pk)

        postSerializer = PostSerializer(post)
        message = f"id: {post.pk}번 포스트 조회 성공"
        return api_response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        
        message = f"id: {pk}번 포스트 삭제 성공"
        return api_response(message = message, status = status.HTTP_200_OK) # 204여도 될 것 같아요


def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

@api_view(['POST'])
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message = f"id: {post.pk}번 포스트 생성 성공"
    return api_response(data = None, message = message, status = status.HTTP_201_CREATED)


def create_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')

        member = Member(
            name = name,
            email = email
        )
        member.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})


def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id' : post.pk,
        '제목' : post.title,
        '내용' : post.content,
        '메세지' : '조회 성공'
    }
    return JsonResponse(data, status=200)


def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
            # 해당 pk의 포스트 삭제
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})


def get_comment(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        comment_list = post.comments.all() # 여기서 comments는 Comment 모델에서 작성한 related_name임
        return HttpResponse(comment_list, status=200)


def like(request, user_id, post_id):
    if request.method == 'PATCH':
        if UserPost.objects.filter(user_id=user_id, post_id=post_id).exists():
            UserPost.objects.filter(user_id=user_id, post_id=post_id).delete()
            return JsonResponse({'message':f'{user_id}의 좋아요가 취소되었습니다.'})
        else:
            userPost = UserPost(
                user_id = user_id,
                post_id = post_id
            )
            userPost.save()
            return JsonResponse(status=204)


def get_likes(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        like_count = UserPost.objects.filter(post_id=post_id).count()
        return JsonResponse({'message':f'{post_id}의 총 하트 수는 {like_count}입니다.'})


def sort_post(request):
    if request.method == 'GET':
        post_list = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count') # Post 객체 모두 가져옴
        # annotate: Post.objects에 추가로 새로운 기능을 추가해줌
        # 여기선 comment_count를 만들어줘서 order_by에 사용함
        # Count('comments')에서 comments는 Comment 객체에서 Post fk 저장할 때 역참조 이름임
        # .order_by를 이용해서 정렬(-는 내림차순 의미함)
        return HttpResponse(post_list, status=200)
