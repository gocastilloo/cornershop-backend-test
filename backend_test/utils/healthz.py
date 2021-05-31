from rest_framework import permissions
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from .models import Ingredients

@api_view(["GET", "HEAD"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def healthz(request, *args, **kwargs):
    """Create menu"""
    return Response(status=200)
