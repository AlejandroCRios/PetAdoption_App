from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper

class Contact(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["nombre","email","telefono","mensaje","ciudad"]
        labels = {
            'telefono': 'Teléfono',
        }
    
    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False    