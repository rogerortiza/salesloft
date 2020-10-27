import os
import requests
from .serializers import PeopleSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from salesloft_project.settings import API_TOKEN_SALESLOFT,\
    API_URL_SALESLOFT


class PeopleViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        A simple ViewSet for listing SalesLoft people
        :param request:
        :return:
        """
        headers = {
            'Authorization': API_TOKEN_SALESLOFT,
            'Accept': 'application/json',
        }
        response = requests.get(url=API_URL_SALESLOFT, headers=headers)
        data = response.json()

        if data:
            try:
                people = data['data']
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = PeopleSerializer(people, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
