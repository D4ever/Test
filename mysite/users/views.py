# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
		return redirect('/users/inornot')
	else:
		form = UserCreationForm()
		ctx = {'form': form}
		ctx.update(csrf(request))
		return render(request, 'register.html', ctx)

def diff_response(request):
	if request.user.is_authenticated():
		content = '<p>my dear user</p>'
	else:
		content = '<p>you wired stranger</p>'
	return HttpResponse(content)

def inorout(request):
	return render(request, 'Loginornot.html')

def user_login(request):
	'''
	login
	'''
	if request.POST:
		username = password = ''
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
#			return specific_user(request)
#			return user_only(request)
#			return diff_response(request)
			return redirect('/users/inornot')
		else:
			return redirect('/users/inornot')			
	ctx = {}
	ctx.update(csrf(request))
	return render(request, 'login.html', ctx)

def name_check(user):
	return user.get_username() == 'admin'

@user_passes_test(name_check)
def specific_user(request):
	return HttpResponse('<p>for admin only</p>')

@login_required
def user_only(request):
	return HttpResponse('<p>This message is for logged in user only.</p>')

def user_logout(request):
	'''
	logout
	URL: /users/logout
	'''
	logout(request)
	return redirect('/users/login')