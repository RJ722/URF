from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
	username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs= dict(required = True, max_length=30)), label = ("Username"), error_messages = { 'invalid': ("This value must contain only letters, numbers and underscores.") })
	email = forms.EmailField(widget=forms.TextInput(attrs = dict(required = True, max_length=30)), label = ("Email Address"))
	password1 = forms.CharField(widget = forms.PasswordInput(attrs = dict(required =True, max_length = 30, render_value=False)), label = ("Password"))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs = dict(required = True, max_length = 30, render_value=False)), label = ("Password Again"))

	def clean_username(self):
		try:
			user = User.objects.get(username__exact = self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(("The username already exists. Please try another one."))

	def clean(self):
			if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
					if self.cleaned_data['password1'] != self.cleaned_data['password2']:
						raise forms.ValidationError(("The two passwords did not match"))
			return self.cleaned_data

