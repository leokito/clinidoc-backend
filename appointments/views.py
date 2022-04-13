from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appointments.models import Appointments
from appointments.serializers import AppointmentSerializer


# Create your views here.
class AppointmentView(APIView):
    def get(self, request):

        # serializer = AppointmentSerializer(data=data)
        appointments = Appointments.objects.all()

        serializer=AppointmentSerializer(appointments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data

        splitted = data['start'].split(":")

        minutes = int(splitted[1])+30

        if (minutes > 59):
           minutes = minutes - 60

        print(minutes)

        data['end'] = splitted[0] +":"+ str(minutes).zfill(2) +":"+ splitted[2]

        serializer = AppointmentSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_appointment = Appointments.objects.create(**data)
        serializer=AppointmentSerializer(new_appointment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)