from django.shortcuts import render, redirect
from .forms import NewUserForm, ChangePasswordForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import user_token


# выводит форму для регистрации нового пользователя
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


# выводит форму для ввода email и высылает на почту письмо со ссылкой для изменения пароля
def reset_password_request(request):
	if request.method == "POST":
		mail = request.POST['mail']
		user = User.objects.filter(email=mail).first()
		if user:
			msg = EmailMultiAlternatives(
				subject='Восстановление пароля в приложении Noted',
				from_email='olga-olechka-5@yandex.ru',
				to=[user.email, ]
			)

			html_content = render_to_string(
				'change_password_letter.html',
				{'domain': get_current_site(request).domain,
				'user': user,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': user_token.make_token(user),
				'protocol': 'https' if request.is_secure() else 'http'}
				)

			msg.attach_alternative(html_content, "text/html")
			msg.send()
			messages.success(request, """Мы отправили вам на электронную почту инструкции по восстановлению пароля. Оно должно прийти в течение нескольких минут. 
										Если вы не получили наше письмо, пожалуйста, проверьте свою папку "спам". """)
			return redirect("login")
		else:
			messages.error(request, "Пользователь с таким email не найден.")
			return redirect("reset_password")
	else:
		return render(request=request, template_name="reset_password_form.html")


# выводит форму для смены пароля, сохраняет изменения в базе данных и логинит пользователя
def password_reset_confirm(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except:
		user = None

	if user is not None and user_token.check_token(user, token):
		if request.method == 'POST':
			form = ChangePasswordForm(user, request.POST)
			if form.is_valid():
				form.save()
				login(request, user)
				messages.success(request, "Пароль успешно изменен.")
				return redirect('main')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)

		form = ChangePasswordForm(user)
		return render(request, 'password_reset_confirm.html', {'form': form})
	else:
		messages.error(request, "Ссылка устарела.")

	messages.error(request, 'Что-то пошло не так. Попоробуйте еще раз зайти на сайт.')
	return redirect("login")