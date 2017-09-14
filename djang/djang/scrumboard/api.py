from rest_framework.generics import ListAPIView

from .serializers import ListSerializer, CardSerializer
from .models import List, Card


#View gets request and retrieve
class ListApi(ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


