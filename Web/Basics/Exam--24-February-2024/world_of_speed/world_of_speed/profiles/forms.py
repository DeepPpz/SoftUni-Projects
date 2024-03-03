from django import forms
from world_of_speed.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        
        widgets = {
              'password': forms.PasswordInput(),
        }

        help_texts = {
            'age': 'Age requirement: 21 years and above.'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
