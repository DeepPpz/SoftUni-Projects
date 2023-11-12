# Generated by Django 4.2.4 on 2023-11-11 21:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_restaurantreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCriticRestaurantReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=5)])),
                ('food_critic_cuisine_area', models.CharField(max_length=100)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
            options={
                'verbose_name': 'Food Critic Review',
                'verbose_name_plural': 'Food Critic Reviews',
                'ordering': ['-rating'],
                'unique_together': {('reviewer_name', 'restaurant')},
            },
        ),
        migrations.CreateModel(
            name='RegularRestaurantReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=5)])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
            options={
                'verbose_name': 'Restaurant Review',
                'verbose_name_plural': 'Restaurant Reviews',
                'ordering': ['-rating'],
                'abstract': False,
                'unique_together': {('reviewer_name', 'restaurant')},
            },
        ),
        migrations.DeleteModel(
            name='RestaurantReview',
        ),
    ]
