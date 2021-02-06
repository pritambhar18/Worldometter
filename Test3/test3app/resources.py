from import_export import resources
from .models import reg_table
from django import forms


class CandidateResource(resources.ModelResource):
    class meta:
        model = reg_table


class SelectionForm(forms.Form):
    selection = forms.ChoiceField(choices=(('CHRT', 'Worldometer Report Charts'), ('BAR', 'Worldometer Report Bars')))
