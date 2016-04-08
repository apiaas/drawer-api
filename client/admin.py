from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client
from .forms import ClientChangeForm, ClientCreationForm


class ClientAdmin(UserAdmin):
    form = ClientChangeForm
    add_form = ClientCreationForm

admin.site.register(Client, ClientAdmin)
