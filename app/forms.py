from django import forms
from .models import Styles, Requisition

class CreateStyleForms(forms.ModelForm):
    class Meta:
        model = Styles
        fields = '__all__'

class UpdateStyleForms(forms.ModelForm):
    class Meta:
        model = Styles
        fields = '__all__'

class searchForms(forms.Form):
    query = forms.CharField(max_length=100)

class RequisitionForms(forms.Form):
    style = forms.ModelChoiceField(
        queryset=Styles.objects.all(),
        empty_label="---SELECT---",
        required=False
    )