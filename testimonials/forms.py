from django import forms
from .models import Tmonials

class TmonialsForm(forms.ModelForm):
    class Meta: 
        model = Tmonials
        fields  = ['name', 'title', 'comment', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget = field.widget
            # Apply Bootstrap classes
            widget.attrs.setdefault('class', 'form-control')
            if name == 'image':
                widget.attrs.setdefault('id', 'image')

