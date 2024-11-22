from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
import requests
from .models import Auther
from .serializers import AutherSerializer

class AutherBooks(APIView):
    def post(self, request):
        auther_data = request.data
        serializer = AutherSerializer(data=auther_data['author'])
        
        if serializer.is_valid():
            validated_data = serializer.validated_data
            
            with transaction.atomic():
                try:
                    author = Auther.objects.create(**validated_data)

                    book_details = {
                        'author_id': str(author.id),
                        'name': auther_data['book']['name'],
                        'price': auther_data['book']['price']
                    }

                    book_resp = requests.post(url='http://127.0.0.1:8002/book/', json=book_details)
                    book_resp.raise_for_status()  
                    
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                except requests.exceptions.RequestException as e:
                    # If there's an error with the Book Service, roll back the transaction
                    return Response({'msg': f'Error with Book Service: {str(e)}'}, status=status.HTTP_502_BAD_GATEWAY)

                except Exception as e:
                    return Response({'msg': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # If serializer is invalid, return the validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
