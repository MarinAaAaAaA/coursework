from django import forms

class CallbackForm(forms.Form):
    name = forms.CharField(required=True, label='Имя')
    phone = forms.CharField(required=True, label='Номер телефона')

mark = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

class RatingForm(forms.Form):
    title = forms.CharField(required=True, label='Ваше имя')
    description = forms.CharField(widget=forms.Textarea(), required=True,label='Ваш вопрос')
    