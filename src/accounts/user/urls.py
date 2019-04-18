from django.contrib import admin
from django.urls import path, re_path, include

from .views import UserDetailAPIView, UserStatusAPIView

urlpatterns = [
    re_path('(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    re_path('(?P<username>\w+)/status/$', UserStatusAPIView.as_view(), name='status-list')
]