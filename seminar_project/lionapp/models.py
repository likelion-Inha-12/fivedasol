from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50) # 50글자가 최대인 문자열
    content = models.TextField(null=True, blank=True) # 글자 수 제한이 없는 긴 문자열
    create_at = models.DateTimeField(auto_now_add=True) # 처음 Post 생성, 현재시간 저장
    member_id = models.ForeignKey(Member, verbose_name="Member", on_delete=models.CASCADE, related_name="posts", null=True)
    # member_id에 null=True를 안해주면 makemigrations 할때 에러발생

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=200, null=True, blank=True)
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments")
    member_id = models.ForeignKey(Member, verbose_name="Member", on_delete=models.CASCADE, related_name="comments", null=True)

    def __str__(self):
        return self.content


class UserPost(models.Model):
    user_id = models.ForeignKey(Member, verbose_name="user", on_delete=models.CASCADE, related_name="user_posts")
    post_id = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE, related_name="user_posts")
# Create your models here.