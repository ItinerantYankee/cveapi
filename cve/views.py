from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cve
from .serializers import CveSerializer
import re

# Create your views here.
@api_view(['GET'])
def get_cve_info(request, cve_id: str):
    # Get all available information on CVE
    # @api_view wrapper adds following functionality: 1) check if HTTP method is allowed, 2) convert request body
    #   into Python data types, 3) convert responses into HTTP response, 4) adds API documentation support

    cve_regex = "^CVE-\d{4}-\d{3,5}$"
    cve_id = cve_id.strip().upper()
    match = re.match(cve_regex, cve_id)
    if match is None:
        return Response({'error': 'Invalid CVE ID.'}, status=400)

    try:
        cve = Cve.objects.get(cve_id=cve_id)
        serializer = CveSerializer(cve, many=False)
        return Response(serializer.data)
    except Cve.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


