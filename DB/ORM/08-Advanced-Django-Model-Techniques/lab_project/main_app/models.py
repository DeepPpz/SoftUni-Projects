from django.db import models
from django.core import validators
import main_app.validations as valids


class ReviewMixin(models.Model):
    rating = models.PositiveIntegerField(validators=[validators.MaxValueValidator(limit_value=5)])
    review_content = models.TextField()

    class Meta:
        abstract = True
        ordering = ['-rating']


class Restaurant(models.Model):
    name = models.CharField(max_length=100, 
                            validators=[validators.MinLengthValidator(2, 'Name must be at least 2 characters long.'),
                                        validators.MaxLengthValidator(100, 'Name cannot exceed 100 characters.')])
    location = models.CharField(max_length=200,
                                validators=[validators.MinLengthValidator(2, 'Location must be at least 2 characters long.'),
                                            validators.MaxLengthValidator(200, 'Location cannot exceed 200 characters.')])
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 validators=[validators.MinValueValidator(0, 'Rating must be at least 0.00.'),
                                             validators.MaxValueValidator(5, 'Rating cannot exceed 5.00.')])


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(validators=[valids.validate_menu_description])
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)


class RestaurantReview(ReviewMixin):
    reviewer_name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
        ordering = ['-rating']
        verbose_name = 'Restaurant Review'
        verbose_name_plural = 'Restaurant Reviews'
        unique_together = ['reviewer_name', 'restaurant']


class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-rating']
        verbose_name = 'Food Critic Review'
        verbose_name_plural = 'Food Critic Reviews'
        unique_together = ['reviewer_name', 'restaurant']


class MenuReview(ReviewMixin):
    reviewer_name = models.CharField(max_length=100)
    menu = models.ForeignKey(to='Menu', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-rating']
        verbose_name = 'Menu Review'
        verbose_name_plural = 'Menu Reviews'
        unique_together = ['reviewer_name', 'menu']
        indexes = [models.Index(fields=['menu'], name='main_app_menu_review_menu_id')]
