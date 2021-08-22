from django import forms
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms.fields import DateField, DecimalField
from .models import Project


class ProjectForm(forms.Form):
    name=forms.CharField(label='Name')
    start=DateField(label='Start',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end=DateField(label='End',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    value=DecimalField(label='Value (in Doller)')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('start', css_class='form-group col-md-4 mb-0'),
                Column('end', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('value',css_class='form-group col-md-6 mb-0'),
            ),
            Submit('pro_submit', 'Create Project', css_class='btn btn-success')
        )
