from django import forms

CITIES_STATE = (
    ('kachin','Kachin'),
    ('kaya','Kaya'),
    ('Kayin','Kayin'),
    ('chin','Chin'),
    ('mon','Mon'),
    ('yangon','Yangon'),
    ('naypyitaw','Nay Pyi Taw'),
    ('Mandalay','Mandalay'),
    ('rakhine','Rakhine')    
)

PAYMENT_CHOICES = (
    ('cbpay','CB Pay'),
    ('kbzpay','KBZ Pay'),
    ('ayapay','AYA Pay'),
    ('cbbank','CB Bank Transfer'),
    ('kbzbank','KBZ Bank Transfer'),
    ('ayabank','AYA Bank Transfer')
)


class AddressForm(forms.Form):
    address = forms.CharField( widget=forms.TextInput(
        attrs= {
            'class':"form-control",
            'placeholder': "1234 Main St",
            'id':"address"
        }
        ), required=True)
    address_2 = forms.CharField( widget=forms.TextInput(
        attrs= {
            'class':"form-control",
            'placeholder': "Apartment or suite",
            'id':"address-2"
        }
        ), required=True)
    cities_state = forms.ChoiceField(
        widget=forms.Select(
                 attrs ={
            'class': 'custom-select d-block w-100'
        }),choices = CITIES_STATE,required=True,      
    )

class PaymentForm(forms.Form):

    payment_opition = forms.ChoiceField(
        widget=forms.Select(
            attrs= {
                'class': 'custom-select d-block w-100' }),choices = PAYMENT_CHOICES,required=True
    )
    file = forms.ImageField(
        widget=forms.FileInput(
            attrs={
            'class':'custom-file-input',
            'id': 'inputGroupFile01'
            }
        ),
        required=True)
    