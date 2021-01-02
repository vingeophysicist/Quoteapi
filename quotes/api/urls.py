from django.urls import path
from quotes.api.views import QuoteListCreateAPIView, QuoteDetailAPIView



urlpatterns = [
    path("quotes/", QuoteListCreateAPIView.as_view(), name="quote-list"),
    path("quotes/<int:pk>/", QuoteDetailAPIView.as_view(), name="quote-detail")

]