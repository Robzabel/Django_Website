from django import forms


class Create_new_list(forms.Form):
    name = forms.CharField(max_length=300, label="name") #label is the form placeholder
    check = forms.BooleanField()

