from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking

def signup_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        p_word = request.POST.get('password')

        if User.objects.filter(username=u_name).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=u_name, email=email, password=p_word)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        user = authenticate(request, username=u_name, password=p_word)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
            
    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def seat_selection(request):  
    movie_name = request.GET.get('name', 'Movie')
    movie_img = request.GET.get('img', '')
    return render(request, 'seats.html', {'movie_name': movie_name, 'movie_img': movie_img})

@login_required(login_url='login')
def payment_view(request):
    if request.method == 'POST':
        m_name = request.POST.get('movie_name')
        m_seats = request.POST.get('seats_selected')
        m_total = request.POST.get('total_amount')

        # This now matches your new models.py exactly
        Booking.objects.create(
            user=request.user,
            movie_name=m_name, 
            seats=m_seats,
            total_amount=m_total
        )
        
        messages.success(request, f"Booking successful for {m_name}!")
        return redirect('dashboard')

    return render(request, 'payment.html')

@login_required(login_url='login')
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-id')
    return render(request, 'my_bookings.html', {'bookings': bookings})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')