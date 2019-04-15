from django.urls import path, re_path, include

from .views import (
        StatusAPIView,
        StatusAPIDetailView
    )

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>', StatusAPIDetailView.as_view()),
]
