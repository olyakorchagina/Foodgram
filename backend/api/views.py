from api.serializers import (FavoriteSerializer, IngredientSerializer,
                             RecipeSerializer, ShoppingCartSerializer,
                             SubscriptionSerializer, TagSerializer,
                             UserSerializer)
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from recipes.models import Favorite, Ingredient, Recipe, ShoppingCart, Tag
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.models import Subscription, User


class PageLimitPaginator(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'limit'
    max_page_size = 10


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    pagination_class = PageLimitPaginator

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        serializer = UserSerializer(
            request.user, context={'request': request}
        )
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=(IsAuthenticated,)
    )
    def subscriptions(self, request):
        queryset = User.objects.filter(subscribers__subscriber=request.user)
        pages = self.paginate_queryset(queryset)
        serializer = SubscriptionSerializer(
            pages, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)

    @action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=(IsAuthenticated,)
    )
    def subscribe(self, request, id):
        subscriber = request.user
        target = get_object_or_404(User, pk=id)

        if request.method == 'POST':
            serializer = SubscriptionSerializer(
                target, data=request.data, context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            Subscription.objects.create(subscriber=subscriber, target=target)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            get_object_or_404(
                Subscription, subscriber=subscriber, target=target
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageLimitPaginator

    #@action(
    #    detail=False,
    #    methods=['GET'],
    #    permission_classes=(IsAuthenticated,)
    #)
    #def download_shopping_cart(self, request):
    #    pass

    @action(
        detail=True,
        methods=['POST'],
        permission_classes=(IsAuthenticated,)
    )
    def shopping_cart(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        data = {
            'user': request.user.id,
            'recipe': recipe.id
        }
        serializer = ShoppingCartSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @shopping_cart.mapping.delete
    def remove_from_cart(self, request, pk):
        get_object_or_404(ShoppingCart, user=request.user.id,
            recipe=get_object_or_404(Recipe, id=pk)
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=['POST'],
        permission_classes=(IsAuthenticated,)
    )
    def favorite(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        data = {
            'user': request.user.id,
            'recipe': recipe.id
        }
        serializer = FavoriteSerializer(
            data=data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @favorite.mapping.delete
    def remove_from_favorite(self, request, pk):
        get_object_or_404(Favorite, user=request.user.id,
            recipe=get_object_or_404(Recipe, id=pk)
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
