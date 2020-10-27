from rest_framework import serializers


class PeopleSerializer(serializers.Serializer):
    """ Serializer for people object """
    display_name = serializers.CharField(max_length=200)
    email_address = serializers.EmailField(max_length=200)
    title = serializers.CharField(max_length=200)
