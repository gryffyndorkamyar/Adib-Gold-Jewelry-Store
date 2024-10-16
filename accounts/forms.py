from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'national_code', 'password1', 'password2')
    
    def clean_national_code(self):
        national_code = self.cleaned_data.get("national_code")
        if not national_code.isdigit():
            raise ValidationError("کد ملی فقط باید عدد باشد")
        
        return national_code


class CustomLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری", max_length=150)
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username or not password:
            raise forms.ValidationError('نام کاربری و رمز عبور هر دو الزامی هستند.')

        return cleaned_data