from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .logic import my_function  # Importa la logica

class MyFunctionView(APIView):
    def post(self, request):
        input_data = request.data.get("input")  # Recupera il dato dall'input
        if input_data is None:
            return Response({"error": "Input data is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        result = my_function(input_data)  # Richiama la funzione
        return Response({"result": result}, status=status.HTTP_200_OK)
