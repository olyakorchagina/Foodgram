from django.core.validators import MinValueValidator
from django.db import models
from users.models import User

MIN_COOK_TIME = 1
MIN_INGREDIENT_AMOUNT = 0.001


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


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )
    image = models.ImageField(
        verbose_name='Фото блюда',
        upload_to='recipes/',
        blank=True,
    )
    text = models.TextField(
        verbose_name='Описание',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
    )
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления (в минутах)',
        validators=[
            MinValueValidator(
                MIN_COOK_TIME,
                f'Минимальное значение: {MIN_COOK_TIME} минута'
            )
        ],
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        default_related_name = 'recipes'
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    amount = models.FloatField(
        verbose_name='Количество',
        validators=[
        MinValueValidator(
            MIN_INGREDIENT_AMOUNT,
            f'Значение должно быть больше 0')
        ],
    )

    class Meta:
        verbose_name = 'Количество ингредиента в рецептe'
        verbose_name_plural = 'Количество ингредиентов в рецептах'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient')
        ]

    def __str__(self):
        return self.ingredient.name


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
