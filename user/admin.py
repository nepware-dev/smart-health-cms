from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Client, Attachment

ADDITIONAL_USER_FIELDS = (
    (_("Additional Fields"), {"fields": ("fhir_patient_id", "fhir_practitioner_id")}),
)


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


admin.site.register(User, CustomUserAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class Attachment(admin.ModelAdmin):
    pass
