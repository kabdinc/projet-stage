from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from apps.authentication.models import Intervenant, Type_user


class AdminSignUpForm(UserCreationForm):
    class Meta:
        model = Intervenant
        fields = ('username', 'email')


class IntervenantAdmin(BaseUserAdmin):
    add_form = AdminSignUpForm
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(Type_user)
admin.site.register(Intervenant, IntervenantAdmin)



