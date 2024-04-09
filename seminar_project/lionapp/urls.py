from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ # seminar_project/urls.py 에 lion/ 으로 지정했기 때문에
# 해당 path는 lion/~~/가 되는거임
    path('create/', views.create_post),
    path('<int:pk>/', views.get_post), # pk라는 변수이름으로 맞춰줘야함
    # views.py 파일에 get_post에서 pk라고 정했기 때문인듯..?
    path('delete/<int:pk>', views.delete_post)
]