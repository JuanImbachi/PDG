# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import DengueCase
from .serializer import DengueCaseSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from model.data_model import Data_Model
import json
from backend.db_connections import mysql_to_csv

mymodel = Data_Model()

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
    except Exception as e:
        res = {
        "code": 0,
        "errMsg": e
        }

    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def updateCSV(request) :
    try :
        mysql_to_csv()
        res = {
            "code":200
        }
    except Exception as e:
        res = {
        "code": 0,
        "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def getPrediction(request):
    try:
        obj = json.loads(request.body)

        city_searched = obj['city']
        neighborhood_searched = obj['neighborhood']
        prediction = mymodel.get_predictions(city_searched, neighborhood_searched, 900, 900)
        res = {
        "code": 200,
        "data": list(prediction)
        }
    except Exception as e:
        res = {
        "code": 0,
        "errMsg": e
        }

    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def getNeighborhoodsToPredict(request, city_searched):
    try:
        
        neighborhoods =  list(DengueCase.objects.filter(City=city_searched).order_by('Neighborhood').values_list('Neighborhood', flat=True).distinct())

        nbh_cases = []
        for neighborhood in neighborhoods:
            numCases = DengueCase.objects.filter(City=city_searched, Neighborhood=neighborhood).count()
            element = [neighborhood, numCases]
            nbh_cases.append(element)

        sorted_nbhs = sorted(nbh_cases, key=lambda x: x[1], reverse=True)[0:4]
        
        selected_nbhds = []
        for neighborhood in sorted_nbhs:
            selected_nbhds.append(neighborhood[0])

        res = {
        "code": 200,
        "data": selected_nbhds
        }
    except Exception as e:
        res = {
        "code": 0,
        "errMsg": e
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

@csrf_exempt
def getNumberCasesByNeighborhoodCityYear(request):
    try:
        obj = json.loads(request.body)

        city_searched = obj['city']
        neighborhoods_searched = obj['neighborhoods']
        years_searched = obj['years']
        finalData = []

        for neighborhood in neighborhoods_searched:
            numCases = DengueCase.objects.filter(City=city_searched, NotificationDate__year__in=years_searched, Neighborhood=neighborhood).count()
            register = [ neighborhood, numCases]
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


