from django.urls import path
from jobs.api.views import JobDetailAPIView, JobsListCreateAPIView

urlpatterns = [
    path("jobs/", JobsListCreateAPIView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobDetailAPIView.as_view(), name="job-detail"),
]
