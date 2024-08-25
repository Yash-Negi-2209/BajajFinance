from django.contrib import admin
from django.urls import path, include
from myapp.views import root_view  # Import the root_view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('process/', include('myapp.urls')),  # Include the /process/ URL
    path('', root_view),  # Set the root URL to be handled by root_view
]
