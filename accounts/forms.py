from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email", "role", "team")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        