from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def root_view(request):
    return HttpResponse("Welcome to the API. Go to /process/ to use the API.")

class ProcessData(APIView):
    def get(self, request):
        return Response({"operation_code": "OP123456789"}, status=status.HTTP_200_OK)

    def post(self, request):
        user_details = {
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123"
        }
        
        data = request.data.get('data', [])
        numbers = []
        alphabets = []
        highest_lowercase = []

        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
                if item.islower():
                    if not highest_lowercase or item > highest_lowercase[0]:
                        highest_lowercase = [item]

        response = {
            "is_success": True,
            "user_id": user_details["user_id"],
            "email": user_details["email"],
            "roll_number": user_details["roll_number"],
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase if highest_lowercase else []  # Handle empty case
        }
        return Response(response, status=status.HTTP_200_OK)
