from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import StartupSubmissionSerializer

class StartupSubmissionAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = StartupSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            submission = serializer.save()
            return Response({
                "message": "Submission received successfully",
                "id": submission.id,
                "founder_name": submission.founder_name,
                "startup_name": submission.startup_name,
                "submitted_at": submission.submitted_at
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        """
        Simple health check endpoint to verify API is working
        """
        return Response({
            "status": "online",
            "message": "API is functioning correctly"
        }, status=status.HTTP_200_OK)