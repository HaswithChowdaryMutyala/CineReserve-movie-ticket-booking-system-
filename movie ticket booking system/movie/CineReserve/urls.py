from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), # Homepage
    # Auth Pages
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # App Logic
    path('', views.dashboard, name='dashboard'), # Homepage
    

    path('seats/', views.seat_selection, name='seats'),
    path('payment/', views.payment_view, name='payment'),
    path('my_booking/', views.my_bookings_view, name='my_booking'),
    path('logout/', views.logout_view, name='logout'),
]