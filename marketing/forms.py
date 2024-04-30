from django import forms
from marketing.models import products
class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = '__all__'