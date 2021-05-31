"""Models based on the menu and users."""
from django.db import models
from django.contrib.auth.models import AbstractUser


class Ingredients(models.Model):
    single_name = models.CharField(
        max_length=50)

    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'nora_ingredients'

    def __str__(self):
        """Returns username"""
        return self.single_name


class Menu(models.Model):
    dish_name = models.CharField(
        max_length=255)

    ingredients = models.ManyToManyField(
        Ingredients,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True,
        help_text="Date time when the dish was created."
    )
    image = models.ImageField(

    )

    class Meta:
        """Meta option."""
        db_table = 'nora_menu'

    def __str__(self):
        """Returns username"""
        return self.dish_name


class User(AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'An user with that email already exists'
        }
    )
    phone_number = models.CharField(
        'Phone number required for slack notifications',
        max_length=17
    )
    is_superuser = models.BooleanField(
        'admin status to perform certain actions',
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    def __str__(self):
        """Returns username"""
        return self.username


class Orders(models.Model):
    """User Based View based on orders."""
    user = models.CharField(
        max_length=255,
        blank=False
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        null=True
    )
    ingredients = models.ManyToManyField(
        Ingredients,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text="Date time when the dish was created."
    )
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        """Returns the order in string format."""
        return f'{self.user} ordena {self.menu} a las {self.created}'


