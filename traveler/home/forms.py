from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Attraction


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ['name', 'region_id', 'attraction_type_id', 'info', 'image_path']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'region_id': forms.Select(attrs={'class': 'form-select'}),
            'attraction_type_id': forms.Select(attrs={'class': 'form-select'}),
            'info': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image_path': forms.FileInput(attrs={'class': 'form-control'}),
        }

