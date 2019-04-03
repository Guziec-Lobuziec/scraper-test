from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

class GloballStats(APIView):
    """

    """

    def get(self, request, format=None):
        return Response({
                'TEONITE': 2311,
                'jest': 3455,
                'super': 4566,
                'tra': 2323,
                'la': 4545,
                'lala': 4545,
                'heja': 8979,
                'ho': 9090,
                'pa': 2323,
                'papa': 4545
            })



class AuthorStats(APIView):
    """

    """

    def get(self, request, author, format=None):
        return Response({
                'TEONITE': 500,
                'jest': 444,
                'super': 333,
                'tra': 234,
                'la': 456,
                'lala': 678,
                'heja': 123,
                'ho': 4564,
                'pa': 55,
                'papa': 345
            })

class Authors(APIView):
    """

    """

    def get(self, request, format=None):
        return Response({
                'andrzejpiasecki': 'Andrzej Piasecki',
                'kamilchudy': 'Kamil Chudy',
                'lukaszpilatowski': 'ukasz Piatowski'
            })
