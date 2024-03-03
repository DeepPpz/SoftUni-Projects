from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 3
    AGE_MIN_VALUE = 21
    PASS_MAX_LENGTH = 20
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25
    
    username = models.CharField(max_length=USERNAME_MAX_LENGTH,
                                validators=[
                                    MinLengthValidator(USERNAME_MIN_LENGTH, 'Username must be at least 3 chars long!'),
                                    RegexValidator(r'^[\w]+$', 'Username must contain only letters, digits, and underscores!')],
                                verbose_name='Username')
    email = models.EmailField(verbose_name='Email')
    age = models.IntegerField(help_text='Age requirement: 21 years and above.',
                              validators=[MinValueValidator(AGE_MIN_VALUE)],
                              verbose_name='Age')
    password = models.CharField(max_length=PASS_MAX_LENGTH,
                                verbose_name='Password')
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True, null=True,
                                  verbose_name='First Name')
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True, null=True,
                                 verbose_name='Last Name')
    profile_picture = models.URLField(blank=True, null=True,
                                      verbose_name='Profile Picture')
