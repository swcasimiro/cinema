from .api import CommentApiViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'comment', CommentApiViewset, basename='comments')

urlpatterns = router.urls

