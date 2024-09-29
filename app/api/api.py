from rest_framework import viewsets
from requests import Response
from cinema.models import Comment

from .serializers import CommentSerializer

class CommentApiViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get']

