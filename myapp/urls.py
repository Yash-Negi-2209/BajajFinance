from django.urls import path
from .views import ProcessData

urlpatterns = [
    path('', ProcessData.as_view(), name='process_data'),  # Handles the root of /process/
]

