import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ready_to_use_django_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ChessPlayer, Meal, Dungeon, Workout
from main_app.models import ArtworkGallery, Laptop


# Create and check models
def show_highest_rated_art():
    searched_art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f'{searched_art.art_name} is the highest-rated art with a {searched_art.rating} rating!'


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    searched_laptop = Laptop.objects.order_by('-price', 'id').first()
    return f'{searched_laptop.brand} is the most expensive laptop available for {searched_laptop.price}$!'


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


def update_operation_systems():
    all_laptops = Laptop.objects.all()
    
    for laptop in all_laptops:
        if laptop.brand == 'Asus':
            laptop.operation_system = 'Windows'
        elif laptop.brand == 'Apple':
            laptop.operation_system = 'MacOS'
        elif laptop.brand == 'Dell' or laptop.brand == 'Acer':
            laptop.operation_system = 'Linux'
        elif laptop.brand == 'Lenovo':
            laptop.operation_system = 'Chrome OS'
        laptop.save()


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__lte=2199).update(title='regular player')


def set_new_chefs():
    all_meals = Meal.objects.all()
    
    for meal in all_meals:
        if meal.meal_type == 'Breakfast':
            meal.chef = 'Gordon Ramsay'
        elif meal.meal_type == 'Lunch':
            meal.chef = 'Julia Child'
        elif meal.meal_type == 'Dinner':
            meal.chef = 'Jamie Oliver'
        elif meal.meal_type == 'Snack':
            meal.chef = 'Thomas Keller'
        meal.save()


def set_new_preparation_times():
    all_meals = Meal.objects.all()
    
    for meal in all_meals:
        if meal.meal_type == 'Breakfast':
            meal.preparation_time = '10 minutes'
        elif meal.meal_type == 'Lunch':
            meal.preparation_time = '12 minutes'
        elif meal.meal_type == 'Dinner':
            meal.preparation_time = '15 minutes'
        elif meal.meal_type == 'Snack':
            meal.preparation_time = '5 minutes'
        meal.save()


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


def show_hard_dungeons():
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')
    end_text = []
    
    for dungeon in hard_dungeons:
        end_text.append(f'{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!')
        
    return '\n'.join(end_text)


def bulk_create_dungeons(*args):
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names():
    all_dungeons = Dungeon.objects.all()
    
    for dungeon in all_dungeons:
        if dungeon.difficulty == 'Easy':
            dungeon.name = 'The Erased Thombs'
        elif dungeon.difficulty == 'Medium':
            dungeon.name = 'The Coral Labyrinth'
        elif dungeon.difficulty == 'Hard':
            dungeon.name = 'The Lost Haunt'
        dungeon.save()


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels():
    all_dungeons = Dungeon.objects.all()
    
    for dungeon in all_dungeons:
        if dungeon.difficulty == 'Easy':
            dungeon.recommended_level = 25
        elif dungeon.difficulty == 'Medium':
            dungeon.recommended_level = 50
        elif dungeon.difficulty == 'Hard':
            dungeon.recommended_level = 75
        dungeon.save()


def update_dungeon_rewards():
    all_dungeons = Dungeon.objects.all()
    
    for dungeon in all_dungeons:
        if dungeon.boss_health == 500:
            dungeon.reward = '1000 Gold'
        elif dungeon.location.startswith('E'):
            dungeon.reward = 'New dungeon unlocked'
        elif dungeon.location.endswith('s'):
            dungeon.reward = 'Dragonheart Amulet'
        dungeon.save()


def set_new_locations():
    all_dungeons = Dungeon.objects.all()
    
    for dungeon in all_dungeons:
        if dungeon.recommended_level == 25:
            dungeon.location = 'Enchanted Maze'
        elif dungeon.recommended_level == 50:
            dungeon.location = 'Grimstone Mines'
        elif dungeon.recommended_level == 75:
            dungeon.location = 'Shadowed Abyss'
        dungeon.save()


def show_workouts():
    searched_workouts = Workout.objects.filter(workout_type__in=['Calisthenics', 'CrossFit'])
    end_text = []
    
    for workout in searched_workouts:
        end_text.append(f'{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!')
    
    return '\n'.join(end_text)


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors():
    all_workouts = Workout.objects.all()
    
    for workout in all_workouts:
        if workout.workout_type == 'Cardio':
            workout.instructor = 'John Smith'
        elif workout.workout_type == 'Strength':
            workout.instructor = 'Michael Williams'
        elif workout.workout_type == 'Yoga':
            workout.instructor = 'Emily Johnson'
        elif workout.workout_type == 'CrossFit':
            workout.instructor = 'Sarah Davis'
        elif workout.workout_type == 'Calisthenics':
            workout.instructor = 'Chris Heria'
        workout.save()


def set_new_duration_times():
    all_workouts = Workout.objects.all()
    
    for workout in all_workouts:
        if workout.instructor == 'John Smith':
            workout.duration = '15 minutes'
        elif workout.instructor == 'Sarah Davis':
            workout.duration = '30 minutes'
        elif workout.instructor == 'Chris Heria':
            workout.duration = '45 minutes'
        elif workout.instructor == 'Michael Williams':
            workout.duration = '1 hour'
        elif workout.instructor == 'Emily Johnson':
            workout.duration = '1 hour and 30 minutes'
        workout.save()


def delete_workouts():
    Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics']).delete()
