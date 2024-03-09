from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


class Profile(models.Model):
    USER_MAX_LENGTH = 15
    USER_MIN_LENGTH = 2
    
    username = models.CharField(max_length=USER_MAX_LENGTH, 
                                validators=[RegexValidator(r'^[\w]+$', 'Ensure this value contains only letters, numbers, and underscore.'),
                                            MinLengthValidator(USER_MIN_LENGTH)],
                                verbose_name='Username')
    email = models.EmailField(verbose_name='Email')
    age = models.PositiveIntegerField(blank=True, null=True, 
                                      verbose_name='Age')
