from django.urls import path, re_path
from .views import (
        UpdateModelDetailApiView,
        UpdateModelListApiView
)
urlpatterns = [
    path('', UpdateModelListApiView.as_view()),
    # re_path(r'^(?P<id>\d+)/$', UpdateModelDetailApiView.as_view()),
    path('<int:id>', UpdateModelDetailApiView.as_view())
]