from django.urls import path

from .views import YouTubeVideoView

urlpatterns = [
    path('', YouTubeVideoView.as_view(), name='youtube_view'),
]
