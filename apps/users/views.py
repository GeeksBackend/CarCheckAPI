from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin, 
                     DestroyModelMixin,
                     CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        return UserSerializer