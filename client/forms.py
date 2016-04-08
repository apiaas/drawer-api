from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Client


class ClientCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    class Meta:
        model = Client
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Client._default_manager.get(username=username)
        except Client.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class ClientChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Client
        fields = '__all__'
