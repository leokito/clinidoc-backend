from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    start = serializers.CharField()
    end = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)