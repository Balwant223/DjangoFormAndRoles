from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout, Submit, Row, Column

class SignInForm(forms.Form):
    username=forms.CharField(label='Username')
    email=forms.EmailField(label='Email',widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput,label='Password')
    password_re=forms.CharField(widget=forms.PasswordInput,label='Re-Enter Password')
    is_manager=forms.BooleanField(label='Manager',required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Row(
                Column('username',css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email',css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password', css_class='form-group col-md-6 mb-0'),
                Column('password_re', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'is_manager',
            Submit('submit', 'Create', css_class='btn btn-primary')
        )
    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_re")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords does not match"
            )


class LogInForm(forms.Form):
    username=forms.CharField(label='Username')
    password=forms.CharField(widget=forms.PasswordInput,label='Password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Row(
                Column('username',css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Login', css_class='btn btn-primary')
        )


class ProjectForm(forms.Form):
    name=forms.CharField(label='Name')
    start=forms.DateField(label='Start',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end=forms.DateField(label='End',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    value=forms.DecimalField(label='Value (in Doller)')
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
