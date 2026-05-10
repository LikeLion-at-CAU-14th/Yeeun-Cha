from django.urls import path
from posts.views import *



urlpatterns = [
    #path('', hello_world, name = 'hello_world'),
    #path('page', index, name='my-page'),
    #path('<int:id>', get_post_detail)

    #path('', post_list, name = "post_list"), # Post 생성, 전체조회
    #path('<int:post_id>/', post_detail, name = "post_detail"), # Post 단일조회
    #path('<int:post_id>/comments/', comment_list, name="comment_list"), # 특정 게시글 댓글 조회
    #path('categories/<str:category_name>/', category_post_list_by_name),
    path('', PostList.as_view()), # post 전체 조회
    path('<int:post_id>/', PostDetail.as_view()), # post 개별 조회
    path('<int:post_id>/comments/', CommentList.as_view()),  # 댓글 목록 조회 + 생성
    path('<int:post_id>/comments/<int:comment_id>/', CommentDetail.as_view()), # 댓글 삭제 
    path('category/', CategoryList.as_view()), # 카테고리 생성 + 조회
]
