from django.shortcuts import render



# Create your views here.

# Equipments view
from django.shortcuts import render
from .models import Equipment

def equipment_view(request):
    equipment_list = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipment_list': equipment_list})


# Most purchased equipments view
from django.shortcuts import render
from django.db.models import Count
from .models import Equipment, Purchase

def most_purchased_equipment(request):
    # Retrieve the most purchased equipment
    most_purchased_equipment = Equipment.objects.annotate(purchase_count=Count('purchase')).order_by('-purchase_count')[:5]

    return render(request, 'equipment/most_purchased_equipment.html', {'most_purchased_equipment': most_purchased_equipment})


# Components view
from django.shortcuts import render
from .models import Component

def component_view(request):
    components = Component.objects.all()
    return render(request, 'components/component_list.html', {'components': components})


# Details of all the purchased equipments view
from django.shortcuts import render
from .models import PurshaseEquipment, Client, Equipment

def purchased_equipment_view(request):
    purchased_equipment = PurshaseEquipment.objects.select_related('equipment', 'user').all()
    return render(request, 'purchased_equipment.html', {'purchased_equipment': purchased_equipment})


# Details of the current user logged-in view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def current_user_details_view(request):
    user_details = {
        'client_id': request.user.id,
        'client_first_name': request.user.first_name,
        'client_last_name': request.user.last_name,
        'client_email': request.user.email,
    }
    return render(request, 'current_user_details.html', {'user_details': user_details})
