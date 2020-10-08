from django import forms
from .models import models
from core.models import Item

CATEGORY_CHOICES = (
    ('E', 'Electronic'),
    ('S', 'Shirt'),
    ('U', 'Utility')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class UploadProductForm(forms.Form):
    title = forms.CharField( widget=forms.TextInput(
        attrs= {
            'class':"form-control",
            'placeholder': "Product Title Here",
            'id':"title"
        }
        ), required=True)
    price = forms.FloatField( widget=forms.TextInput(
        attrs= {
            'class':"form-control",
            'placeholder': "Price : eg 30.0",
            'id':"price"
        }
        ), required=True)

    product_quantity = forms.IntegerField( widget=forms.NumberInput(
        attrs={
            'class' : 'form-control',
            'placeholder': "Quantity : eg : 30",
            'id':"quantity"
        }
    )
    )
    category = forms.ChoiceField(
        widget=forms.Select(
                 attrs ={
            'class': 'custom-select d-block w-100'
        }),choices = CATEGORY_CHOICES,required=True,      
    )
    label = forms.ChoiceField(
        widget=forms.Select(
                 attrs ={
            'class': 'custom-select d-block w-100'
        }),choices = LABEL_CHOICES,required=True,      
    )
    slug = forms.CharField( widget=forms.TextInput(
        attrs= {
            'class':"form-control",
            'placeholder': "Slug Here",
            'id':"slug"
        }
        ), required=True)
    description = forms.CharField( widget=forms.Textarea(
        attrs= {
            'class':"form-control",
            'placeholder': "Product Description Here",
            'id':"product_description"
        }
        ), required=True)
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
            'class':'custom-file-input',
            'id': 'inputGroupFile01',
           }
        ),
        required=True)
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
    
  

