from . import views
from django.urls import path


urlpatterns = [

    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]
