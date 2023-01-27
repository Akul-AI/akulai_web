from django.shortcuts import render

from django.http import JsonResponse
from akulai.akulai import AkulAI

def process_command(request):
    ai = AkulAI()
    command = request.POST.get('command')
    result = ai.process_command(command)
    return JsonResponse({'result': result})
