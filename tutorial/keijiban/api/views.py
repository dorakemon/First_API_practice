from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from keijiban.api.permissions import IsAuthorOrReadOnly

from keijiban.api.serializers import KeijibanSerializer
from keijiban.models import Post

class KeijibanViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Keijiban."""
    queryset = Post.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = KeijibanSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)