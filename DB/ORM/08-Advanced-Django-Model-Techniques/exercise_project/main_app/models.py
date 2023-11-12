from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator


class Customer(models.Model):
    name = models.CharField(max_length=100,
                            validators=[RegexValidator(r'^[A-Za-z ]+$', 'Name can only contain letters and spaces')])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, 'Age must be greater than 18')])
    email = models.EmailField(error_messages={'invalid': 'Enter a valid email address'})
    phone_number = models.CharField(max_length=13,
                                    validators=[RegexValidator(r'^(?:\+359)[0-9]{9}$', 
                                                               "Phone number must start with a '+359' followed by 9 digits")])
    website_url = models.URLField(error_messages={'invalid': 'Enter a valid URL'})


class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']


class Book(BaseMedia):
    author = models.CharField(max_length=100,
                              validators=[MinLengthValidator(5, 'Author must be at least 5 characters long')])
    isbn = models.CharField(max_length=20, unique=True,
                            validators=[MinLengthValidator(6, 'ISBN must be at least 6 characters long')])
    
    class Meta:
        ordering = ['-created_at', 'title']
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'


class Movie(BaseMedia):
    director = models.CharField(max_length=100,
                                validators=[MinLengthValidator(8, 'Director must be at least 8 characters long')])
    
    class Meta:
        ordering = ['-created_at', 'title']
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'


class Music(BaseMedia):
    artist = models.CharField(max_length=100,
                              validators=[MinLengthValidator(9, 'Artists must be at least 9 characters long')])

    class Meta:
        ordering = ['-created_at', 'title']
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def calculate_tax(self):
        return self.price * Decimal('0.08')
    
    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal('2.00')
    
    def format_product_name(self):
        return f'Product: {self.name}'


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return self.price * Decimal('1.20')

    def calculate_tax(self):
        return self.price * Decimal('0.05')
    
    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal('1.50')
    
    def format_product_name(self):
        return f'Discounted Product: {self.name}'


class RechargeEnergyMixin(models.Model):
    class Meta:
        abstract = True
    
    def recharge_energy(self, amount: int):
        self.energy = min(100, self.energy + amount)
        self.save()


class Hero(RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):
    class Meta:
        proxy = True
    
    def swing_from_buildings(self):
        needed_energy = 80
        
        if self.energy <= needed_energy:
            return f'{self.name} as Spider Hero is out of web shooter fluid'
        
        self.energy -= needed_energy
        self.save()
        return f'{self.name} as Spider Hero swings from buildings using web shooters'


class FlashHero(Hero):
    class Meta:
        proxy = True
    
    def run_at_super_speed(self):
        needed_energy = 65
        
        if self.energy <= needed_energy:
            return f'{self.name} as Flash Hero needs to recharge the speed force'
        
        self.energy -= needed_energy
        self.save()
        return f'{self.name} as Flash Hero runs at lightning speed, saving the day'
