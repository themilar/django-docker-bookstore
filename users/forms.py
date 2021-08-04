from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import pgettext, gettext_lazy as _
from django import forms
from django.conf import settings as app_settings
from allauth.account.forms import LoginForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserLogin(LoginForm):
    def __init__(self, *args, **kwargs):
        if app_settings.ACCOUNT_AUTHENTICATION_METHOD == 'username_email':
            login_widget = forms.TextInput(
                attrs={"placeholder": _(
                    "Username or e-mail"), "autocomplete": "email"}
            )
            login_field = forms.CharField(
                label=pgettext("field label", "Username or E-mail"), widget=login_widget
            )
            super(CustomUserLogin, self).__init__(*args, **kwargs)
            self.fields["login"] = login_field
        # return super(CustomUserLogin,self).__init__(*args,**kwargs)
