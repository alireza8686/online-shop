from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}),
        label="نام کاربری"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را وارد کنید"}),
        label="رمز عبور"
    )

    # def clean_user_name(self):
    #     user_name = self.cleaned_data.get("user_name")
    #     is_user_exists = User.objects.filter(username=user_name).exists()
    #     if not is_user_exists:
    #         raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است")

    #     return user_name