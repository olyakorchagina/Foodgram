#from django.core.validators import MinValueValidator
from django.db import models

#from users.models import User


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цветовой hex-код',
        max_length=7,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=50,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


#class IngredientAmount(models.Model):
#    ingredient = models.ForeignKey(
#        Ingredient,
#        verbose_name='Ингредиент',
#        on_delete=models.CASCADE,
#    )
#    amount = models.FloatField(
#        verbose_name='Количество',
#        validators=[
#            MinValueValidator(0.001, 'Значение должно быть больше 0')
#        ],
#    )
#
#    class Meta:
#        ordering = ['ingredient']
#        verbose_name = 'Количество ингредиента'
#        verbose_name_plural = 'Количество ингредиентов'
#
#    def __str__(self):
#        return self.ingredient.name
#
#
#class Recipe(models.Model):
#    author = models.ForeignKey(
#        User,
#        verbose_name='Автор',
#        on_delete=models.CASCADE,
#    )
#    name = models.CharField(
#        verbose_name='Название',
#        max_length=200,
#    )
#    image = models.ImageField(
#        verbose_name='Фото блюда',
#        upload_to='recipes/',
#        blank=True,
#    )
#    text = models.TextField(
#        verbose_name='Описание',
#    )
#    ingredients = models.ManyToManyField(
#        IngredientAmount,
#        verbose_name='Ингредиенты',
#    )
#    tags = models.ManyToManyField(
#        Tag,
#        verbose_name='Теги',
#    )
#    cooking_time = models.IntegerField(
#        verbose_name='Время приготовления (в минутах)',
#        validators=[
#            MinValueValidator(1, 'Минимальное значение — 1')
#        ],
#    )
#    pub_date = models.DateTimeField(
#        verbose_name='Дата публикации',
#        auto_now_add=True,
#    )
#
#    class Meta:
#        default_related_name = 'recipes'
#        ordering = ['-pub_date']
#        verbose_name = 'Рецепт'
#        verbose_name_plural = 'Рецепты'
#
#    def __str__(self):
#        return self.name
#
#
#class ShoppingCart(models.Model):
#    user = models.ForeignKey(
#        User,
#        on_delete=models.CASCADE,
#    )
#    recipe = models.ForeignKey(
#        Recipe,
#        on_delete=models.CASCADE,
#    )
#
#    class Meta:
#        verbose_name = 'Рецепт в списке покупок'
#        verbose_name_plural = 'Рецепты в списке покупок'
#
#
#
#class Favorite(models.Model):
#    user = models.ForeignKey(
#        User,
#        on_delete=models.CASCADE,
#    )
#    recipe = models.ForeignKey(
#        Recipe,
#        on_delete=models.CASCADE,
#    )
#
#    class Meta:
#        verbose_name = 'Рецепт в избранном'
#        verbose_name_plural = 'Рецепты в избранном'
