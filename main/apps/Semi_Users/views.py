from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):

    return render(request, 'SemiUser/index.html', {"users" : User.objects.all()})

def new(request):

	return render(request, 'SemiUser/new.html')

def edit(request, id):


	return render(request, 'SemiUser/Edit.html', {"users" : User.objects.get(id = id )})

def show(request, id):
	return render(request, 'SemiUser/show.html', {"users" : User.objects.get(id = id ).__dict__} )

def create(request):
	errors = User.objects.basic_validator(request.POST)
	print('start')
	if len(errors):
		print('testing')
		for key , value in errors.items():
			messages.error(request, value)
		return redirect('/users/new')
	else:
		print('create')
		User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], 
		email = request.POST['email'])
		messages.success(request, "Successfully created a new user")
		return redirect('/users')

def destroy(request, id):
	User.objects.get(id = id).delete()
	messages.success(request, "Successfully delete a user")
	return redirect('/users')

def update(request, id):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for key , value in errors.items():
			messages.error(request, value)
		return redirect('/users/'+id+'/edit')
	else:
		users = User.objects.get(id = id )
		users.first_name = request.POST['first_name']
		users.last_name = request.POST['last_name']
		users.email = request.POST['email']
		users.save()
		messages.success(request, "User updated successfully")
		return redirect('/users/'+id)


