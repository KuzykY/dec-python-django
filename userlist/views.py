import json

from rest_framework.views import APIView
from rest_framework.response import Response


class UsersListCreateView(APIView):
    def get(self, *args, **kwargs):
        with open('users.json') as file:
            return Response(json.load(file))
