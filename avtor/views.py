# from lib2to3.fixes.fix_input import context
#
# from django.contrib.authen.forms import UserCreationForm
# from django.shortcuts import render
# from django.template.defaultfilters import title
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
#
# # Create your views here.
# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Register")
#         return dict(list(context.items()) + list(c_def.items()))

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/testmain')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/testmain')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль.'})

    # Для метода GET просто возвращаем форму
    return render(request, 'login.html')