from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import BaseUser, RecruiterProfile, AdminProfile


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'name': 'email'})
    )
    password = forms.CharField(
        label='Password',
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'name': 'password'})
    )
    # add remember me checkbox
    remember_me = forms.BooleanField(
        label='Remember me',
        required=False,
        widget=forms.CheckboxInput(attrs={ 'id': 'remember', 'name': 'remember'})
    )

# get the current user model
User = get_user_model()
class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_full_name',
            'name': 'full_name',
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_phone',
            'name': 'phone',
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'id_address',
            'name': 'address',
            'rows': 3,
            'placeholder': 'Your address (optional)',
        })
    )
    photo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'id_photo',
            'name': 'photo',
            'type': 'file',
            'accept': 'image/*',
        })
    )
    
    password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'id_password1',
        'name': 'password1',
    })
    )
    password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'id_password2',
        'name': 'password2',
    })
    )

    
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone', 'address', 'photo', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id':'id_username','name':'username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id':'id_email','name':'email'}),
            }
    
    # now get the extra field from the form then save them into our db
    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.photo = self.cleaned_data.get('photo')
        
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = ['full_name', 'username', 'phone', 'address', 'photo', 'email']
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['photo'].widget.attrs.update({
            'class': 'form-control',
        })



class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['department']
        widgets = {
            'department': forms.TextInput(attrs={'placeholder': 'Your department'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })