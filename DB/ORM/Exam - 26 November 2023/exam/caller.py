import os
import django
from django.db import models


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Article, Review
from django.db.models import Avg



# Django Queries I
def get_authors(search_name, search_email):
    if search_name is None and search_email is None:
        return ""
    
    if search_name and search_email:
        all_searched_objects = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by('-full_name')
    elif search_name:
        all_searched_objects = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')
    elif search_email:
        all_searched_objects = Author.objects.filter(email__icontains=search_email).order_by('-full_name')
    
    if not all_searched_objects:
        return ""
    
    end_result = []
    for author in all_searched_objects:
        end_result.append(f'Author: {author.full_name}, email: {author.email}, status: {"Banned" if author.is_banned else "Not Banned"}')
    
    return '\n'.join(end_result)



def get_top_publisher():
    first_shitty_author = Author.objects.annotate(count=models.Count('articles_authors')).order_by('-count', 'email').first()

    if not first_shitty_author:
        return ""

    if first_shitty_author.count == 0:
        return ""
    
    return f'Top Author: {first_shitty_author.full_name} with {first_shitty_author.count} published articles.'



def get_top_reviewer():
    first_son_of_a_bitch_reviewer = Author.objects.annotate(count=models.Count('reviews_author')).order_by('-count', 'email').first()

    if not first_son_of_a_bitch_reviewer:
        return ""
    
    if first_son_of_a_bitch_reviewer.count == 0:
        return ""
    
    return f'Top Reviewer: {first_son_of_a_bitch_reviewer.full_name} with {first_son_of_a_bitch_reviewer.count} published reviews.'




# Django Queries II
def get_latest_article():
    if not Article.objects.all():
        return ''
    
    latest_lame_article = Article.objects.order_by('-published_on').first()
    retarded_authors = ', '.join(aut.full_name for aut in latest_lame_article.authors.all().order_by('full_name'))
    shitty_reviews = latest_lame_article.reviews_article.all()
    
    shitty_reviews_counter = shitty_reviews.count()
    avg_rating_of_shitty_reviews = shitty_reviews.aggregate(Avg('rating'))['rating__avg'] or 0.0
    
    return f"The latest article is: {latest_lame_article.title}. Authors: {retarded_authors}. Reviewed: {shitty_reviews_counter} times. Average Rating: {avg_rating_of_shitty_reviews:.2f}."



def get_top_rated_article():
    if not Review.objects.all():
        return ''
    
    all_articles_are_bullshit = Article.objects.annotate(avg_lustful_rating=Avg('reviews_article__rating')).order_by('-avg_lustful_rating', 'title').first()
    
    if not all_articles_are_bullshit:
        return ''
    
    num_of_shitty_opinions = all_articles_are_bullshit.reviews_article.count()
    avg_lustful_rating = all_articles_are_bullshit.avg_lustful_rating or 0.0

    if not all_articles_are_bullshit:
        return ''

    return f"The top-rated article is: {all_articles_are_bullshit.title}, with an average rating of {avg_lustful_rating:.2f}, reviewed {num_of_shitty_opinions} times."



def ban_author(email):
    if email is None:
        return 'No authors banned.'
    
    if not Author.objects.all():
        return 'No authors banned.'
    
    try:
        this_bastard_deserves_the_punishment = Author.objects.get(email=email)
    except Author.DoesNotExist:
        return 'No authors banned.'
    
    shitty_opinions = this_bastard_deserves_the_punishment.reviews_author.all()
    num_of_shitty_opinions_deleted = shitty_opinions.count() or 0
    
    this_bastard_deserves_the_punishment.is_banned = True
    this_bastard_deserves_the_punishment.save()
    
    if shitty_opinions:
        shitty_opinions.delete()
    
    return f'Author: {this_bastard_deserves_the_punishment.full_name} is banned! {num_of_shitty_opinions_deleted} reviews deleted.'
