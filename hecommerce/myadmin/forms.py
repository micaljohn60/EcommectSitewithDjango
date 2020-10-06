from django import forms

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
            'placeholder': "Product Title Here",
            'id':"Slug"
        }
        ), required=True)
    description = forms.CharField( widget=forms.Textarea(
        attrs= {
            'class':"form-control",
            'placeholder': "Product Title Here",
            'id':"Product Description Here"
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
    
  

