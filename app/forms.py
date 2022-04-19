"""
Definition of forms.
"""

from django.db import models
from.models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class FeedbackForm(forms.Form):
    login = forms.CharField(label = 'Ваше имя', min_length = 2, max_length = 30)
    gender = forms.ChoiceField(label = 'Ваш пол',
                                choices = [('1', 'Мужской'),('2', 'Женский')],
                                widget = forms.RadioSelect, initial = 1)
    email = forms.EmailField(label = 'Ваш e-mail', min_length = 9)
    buy = forms.BooleanField(label = 'Делали ли вы заказ у данного дилера авто?',
                                required = False)      
    sub = forms.ChoiceField(label = 'Какую оценку дилеру вы бы поставили?',
                                choices = (('1', 'Очень низко'),
                                        ('2', 'Низко'),
                                        ('3', 'Нормально'),
                                        ('4', 'Хорошо'),
                                        ('5', 'Отлично')), initial = 3)
    msg = forms.CharField(label = 'Текст сообщения',
                                widget = forms.Textarea(attrs={'rows':10,'cols':25}))
    prior = forms.ChoiceField(label = 'Достаточно ли удобен сайт для пользователя?',
                                choices = [('1', 'Да'),('2', 'Нет')],
                                widget = forms.RadioSelect, initial = 1)

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}
