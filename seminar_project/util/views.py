from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.response import Response

def health(request):
    return HttpResponse(status = 200, content = "seminar server ok!")

def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)
# Create your views here.
