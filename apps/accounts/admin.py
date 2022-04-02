from django.contrib import admin
from apps.accounts.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from apps.accounts.models import User
# Register your models here.

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ("email",)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        # user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    # add_form_template = "add_form.html"
    list_display = (
        "email",
        "username",
        "phone_number",
        "date_joined",
    )
    ordering = ("email",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    # "is_verified",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    # "is_verified",
                ),
            },
        ),
    )

    filter_horizontal = ()        

admin.site.register(User, CustomUserAdmin)    