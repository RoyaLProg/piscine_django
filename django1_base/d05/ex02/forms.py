from django.forms import Form, CharField


class SimpleForm(Form):
    textField = CharField()
