from rest_framework.response import Response
from rest_framework.views import APIView

from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer


class YouTubeVideoView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "channel": output.channel,
            } for output in YouTubeVideo.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = YouTubeVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
