from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator, ValidationError
from .models import Items

class ItemForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('title', 'title_slug', 'parent', 'menu_name')



    def clean(self):
        root_menu = self.cleaned_data['parent']
        if root_menu != self.cleaned_data['menu_name'] and root_menu.menu_name != self.cleaned_data['menu_name']:
            raise ValidationError('Родитель не свзян с главным меню')
        return super().clean()



