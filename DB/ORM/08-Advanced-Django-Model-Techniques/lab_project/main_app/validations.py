from django.core.exceptions import ValidationError


def validate_menu_description(value):
    required_words = ['Appetizers', 'Main Course', 'Desserts']
    
    for word in required_words:
        if word.lower() not in value.lower():
            raise ValidationError(f'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
