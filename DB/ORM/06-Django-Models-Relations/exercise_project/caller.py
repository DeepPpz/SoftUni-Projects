import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Avg
from datetime import timedelta, date
from main_app.models import Author, Book, Song, Artist, Product, Review
from main_app.models import Driver, DrivingLicense, Owner, Car, Registration


# Create queries within functions
def show_all_authors_with_their_books():
    all_authors = Author.objects.all().order_by('id')
    end_result = []
    
    for author in all_authors:
        books = Book.objects.filter(author=author)
        if books:
            book_titles = ', '.join(book.title for book in books)
            end_result.append(f'{author.name} has written - {book_titles}!')
    
    return '\n'.join(end_result)


def delete_all_authors_without_books():
    all_authors = Author.objects.all()
    authors_to_delete = []
    
    for author in all_authors:
        if not author.book_set.exists():
            authors_to_delete.append(author)
    
    for author in authors_to_delete:
        author.delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    songs = artist.songs.all().order_by('-id')
    return songs


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    
    artist.delete()
    song.delete()


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    avg_rating = Review.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
    return avg_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    all_licenses = DrivingLicense.objects.all().order_by('-license_number')
    end_result = []
    
    for license in all_licenses:
        expiration_date = (license.issue_date + timedelta(days=365)).strftime("%Y-%m-%d")
        end_result.append(f'License with id: {license.license_number} expires on {expiration_date}!')
    
    return '\n'.join(end_result)


def get_drivers_with_expired_licenses(due_date):
    expired_date = due_date - timedelta(days=365)
    end_result = Driver.objects.filter(drivinglicense__issue_date__gte=expired_date)
    return end_result


def register_car_by_owner(owner: object):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return f'Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}.'
