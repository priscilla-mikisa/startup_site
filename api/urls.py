from django.urls import path
from .views import StartupSubmissionAPI

urlpatterns = [
    path('submit/', StartupSubmissionAPI.as_view(), name='submit-startup-api'),
    path('health/', StartupSubmissionAPI.as_view(), name='api-health-check'),
]