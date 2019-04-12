from django.urls import path, re_path, include

from .views import (
        StatusAPIView,
        StatusCreateAPIView,
        StatusDetailAPIView,
        StatusUpdateAPIView,
        StatusDeleteAPIView,
    )

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    #path('<int:id>', StatusDetailAPIView.as_view()),
    re_path(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    path('<int:pk>/update/', StatusUpdateAPIView.as_view()), 
    path('<int:pk>/delete/', StatusDeleteAPIView.as_view()),
]


# /api/status/
# /api/status/create
# /api/status/12/
# /api/status/12/update/
# /api/status/12/delete/