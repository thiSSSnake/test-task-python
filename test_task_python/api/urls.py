from django.urls import path
from .views import AdsListCreateView, AdRetrieveView, AdsListView


# url paths for api
urlpatterns = [
    path('v1/ads/', AdsListView.as_view(), name='ads-list-view'),
    path('v1/ads/create/',
         AdsListCreateView.as_view(),
         name='ads-list-create-view'),
    path('v1/ads/<int:pk>/',
         AdRetrieveView.as_view(),
         name='ads-get-by-id-view'),
]
