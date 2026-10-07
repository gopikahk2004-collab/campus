from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import MaintenanceRequest
from .forms import MaintenanceRequestForm, MaintenanceRequestUpdateForm

def home(request):
    return render(request, 'maintenance/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save(commit=False)
            maintenance_request.user = request.user
            maintenance_request.save()
            messages.success(request, "Maintenance request submitted successfully.")
            return redirect('my_requests')
    else:
        form = MaintenanceRequestForm()
    return render(request, 'maintenance/submit_request.html', {'form': form})

@login_required
def my_requests(request):
    requests = MaintenanceRequest.objects.filter(user=request.user).order_by('-date_reported')
    
    # Filtering
    category = request.GET.get('category')
    priority = request.GET.get('priority')
    status = request.GET.get('status')
    
    if category:
        requests = requests.filter(category=category)
    if priority:
        requests = requests.filter(priority=priority)
    if status:
        requests = requests.filter(status=status)
        
    context = {
        'requests': requests,
        'categories': [c[0] for c in MaintenanceRequest.CATEGORY_CHOICES],
        'priorities': [p[0] for p in MaintenanceRequest.PRIORITY_CHOICES],
        'statuses': [s[0] for s in MaintenanceRequest.STATUS_CHOICES]
    }
    return render(request, 'maintenance/my_requests.html', context)

@login_required
def update_request(request, pk):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, instance=maintenance_request)
        if form.is_valid():
            form.save()
            messages.success(request, "Maintenance request updated successfully.")
            return redirect('my_requests')
    else:
        form = MaintenanceRequestForm(instance=maintenance_request)
    return render(request, 'maintenance/update_request.html', {'form': form})

@login_required
def delete_request(request, pk):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=pk, user=request.user)
    if request.method == 'POST':
        maintenance_request.delete()
        messages.success(request, "Maintenance request deleted successfully.")
        return redirect('my_requests')
    return render(request, 'maintenance/delete_request.html', {'maintenance_request': maintenance_request})

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    requests = MaintenanceRequest.objects.all().order_by('-date_reported')
    return render(request, 'maintenance/staff_dashboard.html', {'requests': requests})

@login_required
@user_passes_test(is_staff)
def update_request_status(request, pk):
    maintenance_request = get_object_or_404(MaintenanceRequest, pk=pk)
    if request.method == 'POST':
        form = MaintenanceRequestUpdateForm(request.POST, instance=maintenance_request)
        if form.is_valid():
            form.save()
            messages.success(request, "Status updated successfully.")
            return redirect('staff_dashboard')
    else:
        form = MaintenanceRequestUpdateForm(instance=maintenance_request)
    return render(request, 'maintenance/update_request_status.html', {'form': form, 'maintenance_request': maintenance_request})
