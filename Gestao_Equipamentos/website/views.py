#views
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import ManagerForm
from django.db import connection
#changes

def registration(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.set_password(form.cleaned_data['password1'])  # Define a senha de forma segura
            manager.save()
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = ManagerForm()
    return render(request, 'registration/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page after successful login
        else:
            # Handle login failure
            return redirect('register')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)  # Logout the user
    return redirect('index')

def password_change(request):
    user = request.user
    # Add any additional context data you want to display on the dashboard
    context = {
        'user': user,
    }
    return render(request, 'perfil.html', context)


def index(request):

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM equipment_view')
        rows = cursor.fetchall()
    
    equipment_list = []

    for row in rows:
        equipment = {
            'id_equip': row[0],
            'equipment_name': row[1],
            'equipment_description': row[2],
            'equipment_price': row[3],
            'equipment_created_at': row[4],
            'type_equip': row[5],
            'equipment_image': row[6],
            'equipment_quantity': row[7],
            'equipment_state': row[8],
            'purchase_count': row[9],
        }

        equipment_list.append(equipment)
    
    context = {
        'equipment_data': equipment_list,
    }

    return render(request, 'index.html', context)

