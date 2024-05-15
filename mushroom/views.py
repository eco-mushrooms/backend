from rest_framework.views import APIView
from rest_framework.response import Response


class MushroomView(APIView):
    def get(self, request):

        return Response({'name': 'mushroom', 'size': 'medium', 'color': 'brown'})
