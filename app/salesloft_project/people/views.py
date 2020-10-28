import os
import requests
from .serializers import PeopleSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from salesloft_project.settings import API_TOKEN_SALESLOFT,\
    API_URL_SALESLOFT


class PeopleViewSet(viewsets.ViewSet):
    """  A simple ViewSet for listing SalesLoft people """
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'email_addresses'
    lookup_value_regex = '[^/]+'

    def _get_query(self, params=''):
        headers = {
            'Authorization': API_TOKEN_SALESLOFT,
            'Accept': 'application/json',
        }
        url = API_URL_SALESLOFT+'/?'+params
        return requests.get(url, headers=headers)

    def list(self, request):
        """
        List  people from SalesLoft
        :param request: context of the request browser
        :return:
        """
        response = self._get_query()
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

    def retrieve(self, request, email_addresses):
        """
        Get one o more people from SalesLoft
        :param request: context of the request browser
        :param email_addresses: lookup_field for query
        :return:
        """
        response = self._get_query(params=email_addresses)
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


class PeopleCountUniqueCharViewSet(PeopleViewSet):
    """  ViewSet to listing SalesLoft people with unique character count dict """

    def _unique_character(self, email):
        """
        Method to return a dict with count of each character base on
        his email
        :param email:  SalesLoft email person
        :return: A dict with count of each unique character
        """
        result = {}

        for ele in email:
            if ele in result:
                result[ele] += 1
            else:
                result[ele] = 1

        return result

    def list(self, request):
        """
        Listing SalesLoft people with dict
        :param request:
        :return:
        """
        response = self._get_query()
        data = response.json()

        if data:
            try:
                people = data['data']
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = PeopleSerializer(people, many=True)
            result = {}

            for person in serializer.data:
                if person['email_address']:
                    result[person['email_address']] = self._unique_character(person['email_address'])
                else:
                    result['display_name'] = 'Not email found'

            return Response(result, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, email_addresses):
        """
          Get one o more people from SalesLoft with dict
        :param request:
        :param email_addresses:
        :return:
        """
        response = self._get_query(params=email_addresses)
        data = response.json()

        if data:
            try:
                people = data['data']
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = PeopleSerializer(people, many=True)
            result = {}
            for person in serializer.data:
                if person['email_address']:
                    result[person['email_address']] = self._unique_character(person['email_address'])
                else:
                    result['display_name'] = 'Not email found'

            return Response(result, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
