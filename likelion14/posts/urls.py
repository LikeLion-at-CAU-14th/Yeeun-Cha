from django.urls import path
from posts.views import *

urlpatterns = [
    #path('', hello_world, name = 'hello_world'),
    #path('page', index, name='my-page'),
    #path('<int:id>', get_post_detail)

    path('', post_list, name = "post_list"), # Post 생성, 전체조회
    path('<int:post_id>/', post_detail, name = "post_detail"), # Post 단일조회
    path('<int:post_id>/comments/', comment_list, name="comment_list"), # 특정 게시글 댓글 조회
    path('categories/<str:category_name>/', category_post_list_by_name)
]