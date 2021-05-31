"""Users views."""
# Django
import datetime
from django.db import IntegrityError
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from backend_test.utils.models import Ingredients, Menu, Orders, User

# Forms
from .forms import MenuForm, OrderForm


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('order')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username and password'})
    return render(request, 'user/login.html')


def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']

        # PASSWORD VALIDATION
        if password != password_confirm:
            error = 'The passwords do not match.'
            return render(request, 'user/signup.html', {'error': error})

        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'user/signup.html', {'error': error})

        # USERNAME VALIDATION
        try:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()

            login(request, user)
            return redirect('order')  # CAMBIAR >> Redireccionar a completar perfil
        except IntegrityError as ie:
            error = f'There is another account using {usermame}'
            return render(request, 'users/signup.html', {'error': error})

    return render(request, 'user/signup.html')


def logout_view(request):
    """Logout an user based on function."""
    logout(request)
    return redirect('login')

@login_required
def upload_menu(request):
    """Admin view based on function."""
    ingredients = Ingredients.objects.all()
    menu = Menu()
    new_ingredient = Ingredients()
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)

            menu.dish_name = data['dish_name']
            menu.description = data['description']
            menu.image = data['image']

            new_ingredient.single_name = data['new_ingredients']
            new_ingredient.save()

            menu.save()

            menu.ingredients.set(data['ingredients'])
        return redirect('order')
    else:
        form = MenuForm()

    return render(
        request=request,
        template_name='menu/upload_menu.html',
        context={
            'form': form,
            'menu': menu,
            'ingredients': ingredients,
        }
    )


class Order(LoginRequiredMixin, View):
    """Class Based View required logged to order menu"""
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        menu = Menu.objects.all()
        form = OrderForm()
        context = {
            'menu': menu,
            'now': now,
            'form': form
        }
        return render(request, 'menu/menu_list.html', context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            order = Orders()
            #menu_qs = Menu.objects.get(pk=pk)

            menu = Menu.objects.all()
            now = datetime.datetime.now()
            print(request.POST.get("id"))

            if form.is_valid():
                data = form.cleaned_data
                order.menu = Menu.objects.get(pk=request.POST.get("id"))
                order.quantity = data['quantity']
                order.user = User.objects.get(username=self.request.user)
                order.save()
                order.ingredients.set(data['ingredients'])


                print(Orders.objects.all())
            else:
                print(form.errors)
            context = {
                'form': form,
                'menu': menu,
                'now': now,
            }
            return render(request, 'menu/menu_list.html', context)
        else:
            return redirect('login')
