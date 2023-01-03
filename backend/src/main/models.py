from django.db import models


class YouTubeVideo(models.Model):
    title = models.CharField(max_length=100)
    channel = models.URLField(max_length=300)
    video_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'
