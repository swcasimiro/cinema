from rest_framework import viewsets
from requests import Response
from rest_framework.views import APIView
from cinema.models import Comment, Video
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CommentSerializer



class CommentApiViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get']

