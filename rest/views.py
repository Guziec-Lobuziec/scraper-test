from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
import urllib
from rest.models import AuthorStatistic, Author, StatsVersion, GloballStatistic


class GloballStats(APIView):
    """

    """

    def get(self, request, format=None):

        versions = StatsVersion.objects \
            .filter(ready = True) \
            .order_by('-version_number')[:1]

        if versions:
            current_version = versions[0]
            return Response(
                {stat.word.word_of_interest: stat.occurance_count
                 for stat in GloballStatistic.objects \
                 .filter(version__version_number=current_version.version_number) \
                 .order_by('-occurance_count')[:10]}
            )
        else:
            return Response({})


class AuthorStats(APIView):
    """

    """

    def get(self, request, author, format=None):

        versions = StatsVersion.objects \
            .filter(ready = True) \
            .order_by('-version_number')[:1]

        if versions:
            current_version = versions[0]
            return Response(
                {stat.word.word_of_interest: stat.occurance_count
                 for stat in AuthorStatistic.objects \
                 .filter(version__version_number=current_version.version_number) \
                 .filter(author__url=urllib.parse.unquote(author)) \
                 .order_by('-occurance_count')[:10]}
            )
        else:
            return Response({})



class Authors(APIView):
    """

    """

    def get(self, request, format=None):

        return Response(
            {author.url: author.full_name for author in Author.objects.all()}
        )
