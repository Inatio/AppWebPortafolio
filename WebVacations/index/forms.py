from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Column, Div, Field,
                                Hidden, Layout, MultiField,
                                Row, Submit, Fieldset)
from django.urls import reverse
from crispy_forms.helper import FormHelper

from .models_new_3 import Usuario, Contacto, Reserva

class UsuarioRegisterForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
                'nombre',
                'correo',
                'celular',
                'contraseña']

        help_texts = {k:"" for k in fields}

class LoginRegisterForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'correo',
            'contraseña']

        help_texts = {k:"" for k in fields}

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = [
            'usuario',
            'descripcion']
    
    widgets = {
        'descripcion': forms.Textarea(
                attrs={
                    'class': '',
                    'autocomplete': 'off',
                    'rows': '8'
                }
            ),
            'user': forms.HiddenInput()
    }
    
    def __init__(self,  *args, **kwargs):

        super().__init__(*args, **kwargs)

        submit_text = "Enviar"

        self.helper = FormHelper()
        self.helper.form_class = 'form-parsley'
        self.helper.layout = Layout(
            Div(
                Row(
                    Column(
                        Row(
                            Column('usuario'),
                            Column('descripcion', css_class='col-md-12'),
                        ),
                        css_class='col-md-12'
                    ),
                    css_class="justify-content-md-center"
                ),
                Row(
                    Column(
                        HTML(
                            '<a class="btn btn-lg btn-warning mr-0 ml-2 my-1 w3-black"'
                            ' href="' + '">'+('Cancelar')+'</a>'
                        ),
                        Submit(
                                'submit', (f'{submit_text} '),
                            css_class='btn btn-primary btn-lg float-right mr-0 ml-2 my-1 w3-button w3-green'),
                        css_class="col-md-10 pt-3 d-flex justify-content-end pt-3 mr-0 "
                    ),
                    css_class="justify-content-md-center"
                )
            )
        )

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = [
            'usuario',
            'departamento',
            'tour',
            'dias']

    widgets = {
        'dias': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'maxlength': "3",
                }
            ),
        'usuario': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        'departamento': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        'tour': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
    }

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        submit_text = "Reservar"

        self.helper = FormHelper()
        self.helper.form_class = 'form-parsley'
        self.helper.layout = Layout(
            Div(
                Row(
                    Column(
                        Row(
                            Column('usuario', css_class='col-md-6'),
                            Column('departamento', css_class='col-md-6'),
                        ),
                        Row(
                            Column('tour', css_class='col-md-6'),
                            Column('dias', css_class='col-md-6'),
                        ),
                        css_class='col-md-12'
                    ),
                    css_class="justify-content-md-center"
                ),
                Row(
                    Column(
                        HTML(
                            '<a class="btn btn-lg btn-warning mr-0 ml-2 my-1 w3-black"'
                            ' href="' + '">'+('Cancelar')+'</a>'
                        ),
                        Submit(
                                'submit', (f'{submit_text} '),
                            css_class='btn btn-primary btn-lg float-right mr-0 ml-2 my-1 w3-green'),
                        css_class="col-md-10 pt-3 d-flex justify-content-end pt-3 mr-0"
                    ),
                    css_class="justify-content-md-center"
                )
            )
        )