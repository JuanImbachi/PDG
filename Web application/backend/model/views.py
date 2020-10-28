# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import DengueCase
from .serializer import DengueCaseSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime, timedelta
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
        neighborhoods_searched = obj['neighborhood']

        finalData = []

        inicio = datetime(2010,1,1).date()
        fin    = datetime(2019,12,31).date()
        lista_fechas = [inicio + timedelta(days=d) for d in range((fin - inicio).days + 1)] 

        for neighborhood in neighborhoods_searched:
            datesFiltered = list(DengueCase.objects.filter(City=city_searched, Neighborhood=neighborhood).values_list('NotificationDate', flat=True).distinct())
        
            for element in lista_fechas:
                if(element in datesFiltered):
                    numCases = DengueCase.objects.filter(City=city_searched, Neighborhood=neighborhood, NotificationDate=element).count()
                    date = element.strftime('%Y-%m-%d')
                    register = [ date, neighborhood, numCases]
                    finalData.append(register)
                else:
                    date = element.strftime('%Y-%m-%d')
                    register = [ date, neighborhood, 0]
                    finalData.append(register)

        res = {
            "code": 200,
            "data":list(finalData)
            }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
            }
    return HttpResponse(json.dumps(res), content_type="application/json")
