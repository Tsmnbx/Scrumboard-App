from rest_framework import serializers


from .models import List, Card


#Model.Serielizer
class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card

        fields = '__all__'

#translates from python to JSON REST
#HyperlinkedModelSerializer
class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = List

        fields = '__all__'




