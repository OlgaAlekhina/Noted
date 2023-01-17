from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login


# вывод формы для регистрации
def register_request(request):
	if request.method == 'POST':
		f = NewUserForm(request.POST)
		if f.is_valid():
			user = f.save()
			login(request, user)
			return redirect('main')

	else:
		f = NewUserForm()

	return render(request, 'registration.html', {'form': f})