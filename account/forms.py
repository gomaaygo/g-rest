from django import forms
from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'password', 'confirm_password', 'type_user', 'email']
        exclude = ["is_staff", "changed_pass", "is_superuser", "user_permissions", "groups", "active", "is_active", "date_joined", 'changed_pass']

    def clean_confirm_password(self):
        if self.data['password'] != self.data['confirm_password'] :
            raise forms.ValidationError("As senhas não são iguais!")

        return self.data['confirm_password']