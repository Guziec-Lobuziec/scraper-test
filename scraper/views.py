from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

class GloballStats(APIView):
    """

    """
    parser_classes = (JSONParser,)

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
