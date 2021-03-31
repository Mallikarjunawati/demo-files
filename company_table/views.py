from django.shortcuts import render
from .models import company_table
import json
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt    
def company_detail(request):
    try:
        company_data=json.loads(request.body)
        print('Step1', company_data)
        company_obj=company_table()
        #return_object=company_data
        print('Step2', company_table)
        if 'company_id' in company_data and company_data['company_id']:
            company_obj.company_id=company_data['company_id']
            print("----->step 3")
        else:
            return_object={
                "message":"company_id required"
            }
            print("------->step 4")
            return JsonResponse(return_object, safe = False) 
        if 'company_name' in company_data and company_data['company_name']:
            company_obj.company_name=company_data['company_name']
            print("------->step 5")
            company_obj.save()
            return_object = {
                "status":0,
                "message":"registraction done successfully"
            }
        else:
            return_object = {
                "message":"company_name required"
            }
            print("---------->step 6")
            return JsonResponse(return_object, safe=False)   
    except Exception as error:
        print("error in company detail",error)
        return_object={
            "message":"Fail to add company details"
        }
    return JsonResponse(return_object, safe=False)


def get_company_detail(request):
    company_data=company_table.objects.all()
    data=list(company_data.values())
    return JsonResponse(data, safe=False)

def get_unique_user(request):
    try:
        unique_data=json.loads(request.body)
        
        if "company_id" in unique_data and unique_data['company_id']:
            find_unique=company_table.objects.filter(company_id=unique_data['company_id'])
            if find_unique:
                data=list(find_unique.values())
                return_object={
                    "status":1,
                    "message":data    
                }
                return JsonResponse(data ,safe=False)
            else:
                return_object={
                    "status":0,
                    "message":"company id not found"
                }
            return JsonResponse(return_object ,safe=False)
    except Exception as error:
        print("Error in get_unique_user" ,error)
        return_object={
            "message":"fail to find"
        }

        


