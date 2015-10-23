from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password',
			ButtonHolder(
				Submit('login', 'Login', css_class='btn-primary')
			)
		)