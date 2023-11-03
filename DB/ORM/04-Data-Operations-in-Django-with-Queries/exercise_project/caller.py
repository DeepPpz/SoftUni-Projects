import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions
def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name, 
        species=species
    )
    
    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    artifacts = Artifact.objects.all()
    artifacts.delete()


def show_all_locations():
    locations = Location.objects.order_by('-id')
    locations_info = []
    for location in locations:
        locations_info.append(f'{location.name} has a population of {location.population}!')
    
    return '\n'.join(locations_info)


def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()


def get_capitals():
    filtered_locations = Location.objects.filter(is_capital=True)
    
    return filtered_locations.values('name')


def delete_first_location():
    first_location = Location.objects.first()
    first_location.delete()


def apply_discount():
    cars = Car.objects.all()
    
    for car in cars:
        percentage_discount = sum(int(x) for x in str(car.year))
        car.price_with_discount = car.price - car.price * percentage_discount / 100
        car.save()

def get_recent_cars():
    recent_cars = Car.objects.filter(year__gte=2020)
    
    return recent_cars.values('model', 'price_with_discount')


def delete_last_car():
    last_car = Car.objects.order_by('-id').first()
    last_car.delete()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)
    tasks_list = []
    
    for task in unfinished_tasks:
        tasks_list.append(f'Task - {task.title} needs to be done until {task.due_date}!')
        
    return '\n'.join(tasks_list)


def complete_odd_tasks():
    odd_tasks = Task.objects.filter(is_finished=False)
    
    for task in odd_tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    encoded_text = ''
    
    for letter in text:
        encoded_text += chr(ord(letter) - 3)
    
    Task.objects.filter(title=task_title).update(description=encoded_text)


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    rooms_info = []
    
    for room in deluxe_rooms:
        if room.id % 2 == 0:
            rooms_info.append(f'Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!')
        
    return '\n'.join(rooms_info)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')
    prev_capacity = None
    
    for room in all_rooms:
        if room.is_reserved is False:
            continue
        
        if prev_capacity is None:
            prev_capacity = room.id
        
        room.capacity += prev_capacity
        room.save()
        prev_capacity = room.capacity


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    
    if last_room.is_reserved is True:
        last_room.delete()


def update_characters():
    all_characters = Character.objects.all()
    
    for character in all_characters:
        if character.class_name == 'Mage':
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == 'Warrior':
            character.hit_points /= 2
            character.dexterity += 4
        else:
            character.inventory = 'The inventory is empty'

        character.save()


def fuse_characters(first_character: object, second_character: object):
    first_inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom' if first_character.class_name in ('Mage', 'Scout') else 'Dragon Scale Armor, Excalibur'
    
    Character.objects.create(
        name = f'{first_character.name} {second_character.name}',
        class_name = 'Fusion',
        level = (first_character.level + second_character.level) // 2,
        strength = (first_character.strength + second_character.strength) * 1.2,
        dexterity = (first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence = (first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points = first_character.hit_points + second_character.hit_points,
        inventory = first_inventory
    )
    
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()
