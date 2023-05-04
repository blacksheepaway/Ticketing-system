from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/new/', views.ticket_create, name='ticket_create'),
    path('ticket/<int:pk>/edit/', views.ticket_update, name='ticket_update'),
    path('accounts/profile/', views.profile, name='profile'),
     path('overview/', views.ticket_overview, name='ticket_overview'),
]
