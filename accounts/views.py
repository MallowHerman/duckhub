from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def loginView(request):
	page = 'login'
	if request.method == 'POST':
		user_email = request.POST.get('user_email').lower()
		user_password = request.POST.get('user_password')
		print(user_email)
		print(user_password)
		try:
			user = User.objects.get(email=user_email)
		except:
			messages.error(request, "O usuário não existe")
            

		authentication_ = authenticate(request, username=user.username, password=user_password)

		if authentication_ is not None:
			 login(request, authentication_)
			 return redirect('frontend:document-list')
		else:
			messages.error(request, 'Email e senha estão incorretos')


	context = {
	'page': page
	}
	return render(request, 'accounts/login_register.html', context)


def registerView(request):
	page = 'register'

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			messages.success(request, "Cadastro realizado com sucesso!")

			return redirect('login')
	else:
		form = UserRegisterForm()

	context = {
	'page': page,
	'form': form
	}
	return render(request, 'accounts/login_register.html', context)



def logoutView(request):
	logout(request)
	return redirect('login')
