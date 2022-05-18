from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import models

import meilisearch
import json

search_client = meilisearch.Client('http://127.0.0.1:7700')

class DateEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self,obj)


def userlogin(request):
    return HttpResponse(json.dumps("test"), content_type="application/json")

def format(data=[], code = 20060, msg = 'success'):
    return json.dumps({"code": code, "message": msg,"data":data},cls=DateEncoder)


@require_http_methods(['POST'])
def search(request):
    postBody = request.body
    json_result = json.loads(postBody)
    # print(json_result)
    keyword = json_result['keyword']
    # print(keyword)
    try:
        res = search_client.index('vulnerabilities').search(keyword)
        print(res, type(res))
    except Exception as e:
        print("meilisearch failed, check the network or the meilisearch server.")
        print(e)
        return HttpResponse(format(code=20000))
    return HttpResponse(format(data=res))

