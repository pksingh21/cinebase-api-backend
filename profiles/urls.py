from django.urls import path
from profiles.views import ProfileList

urlpatterns = [
    path("<int:pk>/", ProfileList.as_view()),
]
