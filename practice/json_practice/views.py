from django.http import JsonResponse
from django.shortcuts import render
import json, requests, request


def get_json():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = json.loads(response.text)
    print(users == response.json())
    #print(type(users))
    print(users[:1])
    #json_string = json.dumps(users)

get_json()

#def get_page():
#     return render(request, 'parcing.html')
