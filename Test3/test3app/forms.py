from django import forms
from .models import reg_table
from .models import log_table

class reg_tableForm(forms.ModelForm):
    class Meta:
        model = reg_table
        fields = "__all__"

class log_tableForm(forms.ModelForm):
    class Meta:
        model = log_table
        fields = "__all__"