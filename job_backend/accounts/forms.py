from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, Role

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'role', 'password1', 'password2')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'role')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'avatar', 'role', 'email', 'phone', 'address', 'city', 'state', 'country', 'zip_code', 'about_me', 'resume', 'linkedin', 'github', 'twitter', 'facebook', 'instagram', 'youtube', 'website', 'blog', 'company_name', 'company_logo', 'company_website', 'company_address', 'company_city', 'company_state', 'company_country', 'company_zip_code', 'company_phone', 'company_fax', 'company_about', 'company_facebook', 'company_twitter', 'company_linkedin', 'company_instagram', 'company_youtube', 'company_blog', 'company_youtube')