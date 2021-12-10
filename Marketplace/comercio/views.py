
from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId

# -----------------------------------------------------


@api_view(["GET", "POST"])
def comercio(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    place = db['comercio']
    if request.method == "GET":
        result = []
        data = place.find({})
        for dto in data:
            json_data = {
                "id": str(dto['_id']),
                "nombre": dto['nombre'],
                'sede': dto['sede'],
            }
            result.append(json_data)
        client.close()
        return JsonResponse(result, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        measurements = []
        data['sede'] = measurements
        result = place.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)

# --------------------------------------------------

@api_view(["GET", "POST", "DELETE"])
def comercio_detail(request, pk):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    place = db['comercio']
    if request.method == "GET":
        result = []
        data = place.find({'_id': ObjectId(pk)})
        for dto in data:
            json_data = {
                "id": str(dto['_id']),
                "nombre": dto['nombre'],
                'sede': dto['sede'],
            }
            result.append(json_data)
        client.close()
        return JsonResponse(result[0], safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)

        json_data = {
            'ubicacion': data["ubicacion"],
            'puntos': data["puntos"],
        }

        place_post = place.find({'_id': ObjectId(pk)})
        for dto in place_post:
            for d in dto["sede"]:
                if d["sede"] == data["sede"]:
                    d["sede"].append(json_data)
                    result = place.update(
                        {'_id': ObjectId(pk)},
                        {'$set': {'comercio': dto["comercio"]}}
                    )
                    respo = {
                        "MongoObjectID": str(result),
                        "Mensaje": "Se añadió una nueva medida"
                    }
                    client.close()
                    return JsonResponse(respo, safe=False)

        json_data_new = {
            'sede': data["sede"],
            'values': [
                json_data
            ]
        }
        result = place.update(
        {'_id': ObjectId(pk)},
        {'$push': {'measurements': json_data_new}}
        )
        respo = {
            "MongoObjectID": str(result),
            "Mensaje": "Se añadió una nueva medida"
        }
        client.close()
        return JsonResponse(respo, safe=False)

    if request.method == "DELETE":
        result = place.remove({"_id": ObjectId(pk)})
        respo = {
            "MongoObjectID": str(result),
            "Mensaje": "Se ha borrado un lugar"
        }
        client.close()
        return JsonResponse(respo, safe=False)

# -----------------------------------------------------

@api_view(["POST"])
def average(request, pk):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    place = db['comercio']
    data = place.find({'_id': ObjectId(pk)})
    result = []
    variable_name = ""

    # Calculo de promedio
    average = 0
    for dto in data:
        place = dto["sede"]
        average += place["puntos"]

    average /= len(data)

    json_data = {
        "place": place,
        "variable": variable_name,
        "average": average
    }
    result.append(json_data)
    client.close()
    return JsonResponse(result[0], safe=False)
