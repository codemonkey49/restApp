from django import forms

class instanceIDForm(forms.Form):
    instanceID=forms.CharField(label="instance ID:",max_length=20)
    name=forms.CharField(label="name:", max_length=10)

