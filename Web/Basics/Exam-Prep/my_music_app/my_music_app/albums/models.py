from django.db import models
from django.core.validators import MinValueValidator
from my_music_app.profiles.models import Profile


class Album(models.Model):
    NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.0
    
    
    GENRES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'), 
        ('Hip Hop Music', 'Hip Hop Music'), 
        ('Other', 'Other'),
    )
    
    album_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True, 
                                  verbose_name='Album Name')
    artist = models.CharField(max_length=ARTIST_MAX_LENGTH, 
                              verbose_name='Artist')
    genre = models.CharField(max_length=GENRE_MAX_LENGTH, choices=GENRES, 
                             verbose_name='Genre')
    description = models.TextField(blank=True, null=True, 
                                   verbose_name='Description')
    image_url = models.URLField(verbose_name='Image URL')
    price = models.FloatField(validators=[MinValueValidator(PRICE_MIN_VALUE)], 
                              verbose_name='Price')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, 
                              verbose_name='Owner')
