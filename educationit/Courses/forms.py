from django import forms

from .models import Courses


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'description', 'duration', 'duration_unit', 'icon_link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input_text'}),
            'description': forms.Textarea(attrs={'class': 'input_text'}),
            'duration': forms.NumberInput(attrs={'class': 'input_text'}),
            'duration_unit': forms.Select(attrs={'class': 'input_select'}),
            'icon_link': forms.TextInput(attrs={'class': 'input_text'}),
        }
        labels = {
            'name': 'Название курса',
            'description': 'Описание',
            'duration': 'Продолжительность',
            'duration_unit': 'Единица измерения продолжительности',
            'icon_link': 'Ссылка на иконку',
        }
