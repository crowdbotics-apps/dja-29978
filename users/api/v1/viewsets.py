from rest_framework import authentication
from users.models import Trainer
from .serializers import TrainerSerializer
from rest_framework import viewsets


class TrainerViewSet(viewsets.ModelViewSet):
    serializer_class = TrainerSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Trainer.objects.all()
