from django.contrib import admin
from recipes.models import Ingredient, Recipe, RecipeIngredient, Tag


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
    )
    list_filter = (
        'name',
        'author',
        'tags',
    )
    search_fields = (
        'name',
        'author',
    )
    empty_value_display = '-пусто-'


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'ingredient',
        'recipe',
        'amount',
    )
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
    )
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
    )
    empty_value_display = '-пусто-'

admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
