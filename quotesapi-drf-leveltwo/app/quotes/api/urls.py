from django.urls import path
from quotes.api.views import QuoteDetailAPIView, QuoteListCreateAPIVIEW

urlpatterns = [
    path("quotes/", QuoteListCreateAPIVIEW.as_view(), name="quote-list"),
    path("quotes/ziny:pk>/", QuoteDetailAPIView.as_view, name="quote-detail"),
]
