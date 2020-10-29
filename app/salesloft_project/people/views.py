import operator
from collections import OrderedDict
import requests
from .serializers import PeopleSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from salesloft_project.settings import API_TOKEN_SALESLOFT,\
    API_URL_SALESLOFT


class BasicPeopleViewSet(viewsets.ViewSet):
    """  Basic ViewSet SalesLoft people """
    permission_classes = [IsAuthenticated]
    lookup_field = 'email_addresses'
    lookup_value_regex = '[^/]+'

    def _unique_character(self, email):
        """
        Method to return a dict with count of each character base on
        his email
        :param email:  SalesLoft email's person
        :return: A dict with unique character count
        """
        result = {}

        for ele in email:
            if ele in result:
                result[ele] += 1
            else:
                result[ele] = 1

        return OrderedDict(sorted(result.items(),
                                  key=operator.itemgetter(1),
                                  reverse=True))

    def _get_query(self, params=''):
        """
        Private method to perform queries in SalesLoft API
        :param params: value to filter the data
        :return: a response from SalesLoft API
        """
        headers = {
            'Authorization': API_TOKEN_SALESLOFT,
            'Accept': 'application/json',
        }
        url = API_URL_SALESLOFT + '/?' + params
        return requests.get(url, headers=headers)

    def _send_response(self, response=None, unique_character=False):
        """
        Private method to perform responses from SalesLoft Project
        to web client
        :param response: the response from SalesLoft API
        :param unique_character: True or False. If true create a unique
        character dict and its added to the response
        :return:  a response from SalesLoft Project
        """
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            try:
                people = data['data']
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = PeopleSerializer(people, many=True)
            response = serializer.data

            if unique_character:
                result = []
                for person in serializer.data:
                    res = {}
                    if person['email_address']:
                        res['display_name'] = person['display_name']
                        res['email_address'] = person['email_address']
                        res['unique_character'] = \
                            self._unique_character(
                                email=person['email_address'])
                    else:
                        res['display_name'] = 'Not email found'
                    result.append(res)

                response = result

            return Response(response, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PeopleViewSet(BasicPeopleViewSet):
    """ ViewSet SalesLoft people """

    def list(self, request):
        """
        List  people from SalesLoft
        :param request: context of the request browser
        :return:
        """
        response = self._get_query()
        return self._send_response(response)

    def retrieve(self, request, email_addresses):
        """
        Get one o more people from SalesLoft
        :param request: context of the request browser
        :param email_addresses: lookup_field for query
        :return:
        """
        response = self._get_query(params=email_addresses)
        return self._send_response(response)


class PeopleCountUniqueCharViewSet(BasicPeopleViewSet):
    """
    ViewSet to listing SalesLoft people with unique character
    count dict
    """

    def list(self, request):
        """
        Listing SalesLoft people with dict
        :param request:
        :return:
        """
        response = self._get_query()
        return self._send_response(response, unique_character=True)

    def retrieve(self, request, email_addresses):
        """
          Get one o more people from SalesLoft with dict
        :param request:
        :param email_addresses:
        :return:
        """
        response = self._get_query(params=email_addresses)
        return self._send_response(response, unique_character=True)
