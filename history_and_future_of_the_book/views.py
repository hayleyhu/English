from django.shortcuts import render
from django.utils import timezone
from .models import Table
from .forms import UserForm
#from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	tables = Table.objects.all()
	return render(request, 'history_and_future_of_the_book/index.html', {'action':'Display all tables', 'tables':tables})

def register(request):
	#ontext = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
	return render(request, 'history_and_future_of_the_book/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Your account is disabled.')
		else:
			print ("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'history_and_future_of_the_book/login.html', {})

@login_required
def requesttoedit(request):
	return HttpResponse("Since you're logged in, you can submit a request to edit the archive!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')



