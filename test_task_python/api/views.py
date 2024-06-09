from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import AdsSerializer
from .models import Ads


class AdsListCreateView(generics.CreateAPIView):
    '''The view is used
    to to add new data using a POST request.
    Only an authorized user can add data.'''

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (IsAuthenticated, )


class AdsListView(generics.ListAPIView):
    '''The view is used to get data from latest 10 ads(by position)
    Only an authorized user can get data'''
    queryset = Ads.objects.all().order_by('position')[:10]
    serializer_class = AdsSerializer
    permission_classes = (IsAuthenticated, )


class AdRetrieveView(generics.RetrieveAPIView):
    '''Getting ad data using the transmitted ad id
    Only an authorized user can get data'''
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    lookup_field = "pk"
    permission_classes = (IsAuthenticated, )
