from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from world_of_speed.profiles.models import Profile
from world_of_speed.cars.custom_validators import validate_year_range


class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    MODEL_MAX_LENGTH = 15
    MODEL_MIN_LENGTH = 1
    PRICE_MIN_VALUE = 1.0
    
    TYPES = (
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    )
    
    type = models.CharField(max_length=TYPE_MAX_LENGTH, choices=TYPES, 
                            verbose_name='Type')
    model = models.CharField(max_length=MODEL_MAX_LENGTH,
                             validators=[MinLengthValidator(MODEL_MIN_LENGTH)],
                             verbose_name='Model')
    year = models.IntegerField(validators=[validate_year_range],
                               verbose_name='Year')
    image_url = models.URLField(unique=True,
                                error_messages={
                                    'unique': "This image URL is already in use! Provide a new one."},
                                verbose_name='Image URL')
    price = models.FloatField(validators=[MinValueValidator(PRICE_MIN_VALUE)],
                              verbose_name='Price')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              verbose_name='Owner')
