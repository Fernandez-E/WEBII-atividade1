from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def mult(require):
    op1=require.GET.get("op1", "")
    op2=require.GET.get("op2", "")
    res={}
    res["resultado"] = float(op1)*float(op2)
    return JsonResponse(res)