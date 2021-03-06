from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Contact, Event, Profile

alpha = RegexValidator(r"^[A-zÀ-ž\s']*$", 'Les charactères numériques sont interdit.')
alphanumeric = RegexValidator(r"^['0-9a-zA-Z]*$", 'Charactères interdit')
numeric = RegexValidator(r"^[0-9+-]*$", 'Les caractères alpha sont interdit.')


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        label= '',
        validators=[alpha],
        error_messages={'required': 'Ce champ est obligatoire.'},
        widget=forms.TextInput(
            attrs={
                "placeholder":"Nom",
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control"
            }
        )
    )

    mail = forms.EmailField(
        label='',
        error_messages={'required': 'Ce champ est obligatoire.'},
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "placeholder": "Mail",
                "oninvalid": "this.setCustomValidity('Entrer une adresse email')",
                "oninput": "setCustomValidity('')",
                "class": "form-control"
            }
        )
    )
    
    message = forms.CharField(
        label='',
        error_messages={'required': 'Ce champ est obligatoire.'},
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message",
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control",
                "rows": "5"
            }
        )
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'mail',
            'message'
        ]

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        max_length=150,
        label='Nom d\'utilisateur'
    )

    password = forms.CharField(
        max_length=300,
        label='Mot de passe',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'password', )

class ResetPasswordForm(PasswordResetForm):

    email = forms.CharField(
        required=True,
        max_length=300,
        label='Adresse email',
        widget=forms.TextInput(
            attrs={
                "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
                "oninput": "setCustomValidity('')",
                "class": "form-control"
            })

    )

class SignUpForm(UserCreationForm):

    username = forms.CharField(
        max_length=150,
        label='Nom d\'utilisateur'
    )

    first_name = forms.CharField(
        max_length=50,
        required=True,
        label='Prenom'
    )

    last_name = forms.CharField(
        max_length=50,
        required=True,
        label='Nom'
    )

    email = forms.EmailField(
        max_length=254
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Mot de passe'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirmation de mot de passe'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class MemberForm(forms.ModelForm):
#
#     status=[
#         ('','Choisissez un Statut'),
#         ('étudiant','Étudiant'),
#         ('salarié','Salarié'),
#         ('entrepreneur','Entrepreneur'),
#         ('autre','Autre'),
#     ]
#
#     name = forms.CharField(
#         required=True,
#         label='',
#         validators=[alpha],
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder":"Nom",
#                 "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
#                 "oninput": "setCustomValidity('')",
#                 "class": "form-control",
#                 "pattern": "([A-zÀ-ž\s']){2,}"
#             }
#         )
#     )
#
#     mail = forms.CharField(
#         required=True,
#         label='',
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Mail",
#                 "oninvalid": "this.setCustomValidity('Ce champ est obligatoire')",
#                 "oninput": "setCustomValidity('')",
#                 "class": "form-control"
#             })
#     )
#
#     phone_number    = forms.CharField(
#         required=False,
#         label='',
#         validators=[numeric],
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Téléphone",
#                 "oninvalid": "this.setCustomValidity('Entré une information valide')",
#                 "oninput": "setCustomValidity('')",
#                 "class": "form-control",
#             })
#     )
#
#     status = forms.ChoiceField(
#         error_messages={'required': 'Choisissez une option dans la liste'},
#         required=True,
#         label='',
#         initial='none',
#         choices=status,
#         widget=forms.Select(
#             attrs={
#                 "oninvalid": "this.setCustomValidity('Choisissez une option dans la liste')",
#                 "oninput": "setCustomValidity('')",
#                 "class": "form-control"
#             })
#         )
#
#     first_year = forms.CharField(
#         label='Première Année ?',
#         required=False,
#         widget=forms.CheckboxInput(
#             attrs={
#                 "class": "form-check-input",
#             }
#         )
#     )
#
#     class Meta:
#         model = Member
#         fields = [
#             'name',
#             'mail',
#             'phone_number',
#             'status',
#             'first_year'
#         ]