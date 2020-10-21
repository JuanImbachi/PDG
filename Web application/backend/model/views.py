# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import DengueCase
from .serializer import DengueCaseSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def casesFilter( request):
    try:
        obj = json.loads(request.body)

        city_searched = obj['city']
        year_searched = obj['years']
        neighborhood_searched = obj['neighborhoods']

        res = {
        "code": 200,
        "data": serializers.serialize("json",DengueCase.objects.filter(City=city_searched, NotificationDate__year__in=year_searched, Neighborhood__in=neighborhood_searched))
        }
    except Exception :
        res = {
        "code": 0,
        "errMsg": "Sorry for you"
        }

    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def getNeighborhoodsByCity(request, city_searched):
    try:
        res = {
        "code": 200,
        "data": list(DengueCase.objects.filter(City=city_searched).order_by('Neighborhood').values_list('Neighborhood', flat=True).distinct())
        }
    except Exception as e:
        res = {
        "code": 0,
        "errMsg": e
        }

    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def getCasesByCityNeighborhood(request):
    try:
        obj = json.loads(request.body)
        city_searched = obj['city']
        neighborhood_searched = obj['neighborhood']
        finalData = []
        dates = list(DengueCase.objects.filter(City=city_searched, Neighborhood=neighborhood_searched).order_by('NotificationDate').values_list('NotificationDate', flat=True).distinct())

        for dd in dates:
            numCases = DengueCase.objects.filter(NotificationDate=dd).count()
            date = dd.strftime('%Y/%m/%d')
            register = [ date, numCases]
            finalData.append(register)

        res = {
        "code": 200,
        "data": list(finalData)
        }
    except Exception as e:
        res = {
        "code": 0,
        "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

