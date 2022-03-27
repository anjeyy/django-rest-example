from django.urls import path

from .views import DocumentViews

urlpatterns = [
    path('documents/', DocumentViews.as_view()),
    path('documents/<int:id>', DocumentViews.as_view())
]
