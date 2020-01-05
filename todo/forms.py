from django import forms


class TodoForms(forms.Form):
    text = forms.CharField(max_length=60,
    widget=forms.TextInput(
    attrs ={
    'class':'DjangoTodo',
    'placeholder':'Django Todo',
    }))
