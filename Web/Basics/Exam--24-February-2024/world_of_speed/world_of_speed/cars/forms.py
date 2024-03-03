from django import forms
from world_of_speed.cars.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

        widgets = {
            'image_url': forms.URLInput(attrs={
                'placeholder': 'https://...'
                })
        }


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)


class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
