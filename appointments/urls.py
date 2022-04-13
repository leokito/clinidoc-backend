from django.contrib import admin
from django.urls import path

from appointments.views import AppointmentView

urlpatterns = [
    path('appointments/', AppointmentView.as_view()),
]
