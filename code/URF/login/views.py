from django.shortcuts import render

# Create your views here.
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def register(request):
	print("Checking for a POST request")
	if request.method == 'POST':
		print ("Post request found")
		print ("Sending data to the registartion Form")
		form = RegistrationForm(request.POST)
		print ("Form recieved!")
		print ("Form is ", form)
		if form.is_valid():
			print ("Form is valid")
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
			)
			print ("Hurra, user is created amd we are now redirecting towards /register/success")
			return HttpResponseRedirect('/register/success/')
		else:
			print ("Form is not valid")
	else:
		form = RegistrationForm()
		print ("Form is not making a POST request")

	#print ("Displaying the registration page, 'variables' at the time is", variables)
	return render(request, 'registration/register.html', {'form' : form })

def register_success(request):
	return render_to_response('registration/success.html', )

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def home(request):
	return render_to_response('home.html', { 'user' : request.user }, )
