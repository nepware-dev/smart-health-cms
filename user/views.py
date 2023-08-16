from rest_framework import viewsets, mixins

from user.models import Attachment
from user.serializers import AttachmentSerializer


class AttachmentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
