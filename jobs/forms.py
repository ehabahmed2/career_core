from django import forms
from .models import Job,CandidateDetails
from django.forms.widgets import CheckboxInput, TextInput, EmailInput


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'price', 'location', 'is_active', 'is_remote', 'description', 'job_type', 'experience']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'id': 'id_is_active', 'name': 'is_active', 'type':'checkbox'}),
            'is_remote': forms.CheckboxInput(attrs={'id': 'id_is_remote'}),
            # you can add other widget overrides here if you like
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, CheckboxInput):
                # Bootstrap style for checkboxes
                widget.attrs.setdefault('class', 'form-check-input')
            else:
                # Bootstrap style for text inputs, selects, etc.
                widget.attrs.setdefault('class', 'form-control')

            # force required on _every_ field
            if name != 'is_remote' and name == 'location':
                field.required = True



class CandidateApplicationForm(forms.ModelForm):
    class Meta:
        model = CandidateDetails
        fields = [
            'full_name',
            'whatsapp',
            'email',
            'education',
            'age',
            'location',
            'other_language_1',
            'other_language_2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget = field.widget
            # Apply Bootstrap classes
            if isinstance(widget, CheckboxInput):
                widget.attrs.setdefault('class', 'form-check-input')
            else:
                widget.attrs.setdefault('class', 'form-control')

            # Make all fields required except these two
            if name not in ('other_language_1', 'other_language_2'):
                field.required = True

