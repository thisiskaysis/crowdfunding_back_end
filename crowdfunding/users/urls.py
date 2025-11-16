from django.urls import path
from . import views

urlpatterns = [
    # User registration
    path('', views.CustomUserRegister.as_view(), name='user-register'),
    path('<int:pk>/', views.CustomUserDetail.as_view(), name='user-detail'),
    # Child management
    path('', views.ChildList.as_view(), name='child-list'),
    path('<int:pk>/', views.ChildDetail.as_view(), name='child-detail')
]