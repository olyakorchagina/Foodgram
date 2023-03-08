from api.mixins import CreateListRetrieveViewSet
from api.serializers import (IngredientSerializer, SetPasswordSerializer,
                             TagSerializer, UserSerializer)
from recipes.models import Ingredient, Tag
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User


class PageLimitPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 10


class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes
    pagination_class = PageLimitPaginator


    @action(
        detail=False,
        methods=['GET'],
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['POST'],
        permission_classes=(IsAuthenticated,)
    )
    def set_password(self, request):
        serializer = SetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            current_password = serializer.data.get('current_password')
            new_password = serializer.data.get('new_password')
            if not user.check_password(current_password):
                return Response({'current_password': ['Неверный пароль']})
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors)

    #@action(
    #    detail=False,
    #    methods=['GET'],
    #    permission_classes=(IsAuthenticated,)
    #)
    #def subscriptions(self, request):
    #    pass

    #@action(
    #    detail=True,
    #    methods=['POST', 'DELETE'],
    #    permission_classes=(IsAuthenticated,)
    #)
    #def subscribe(self, request, pk):


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
