from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def say_hello(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			# log the user in
			messages.success(request, "You have been logged in")
			return redirect('home')
		else: # send the user back to the login page
			messages.error(request, 'Invalid username or password')
			return redirect('home')
	else:
		return render(request, 'home.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, 'You have been logged out...')
	return redirect('home')