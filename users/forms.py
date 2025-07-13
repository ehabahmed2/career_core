from django import forms


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


