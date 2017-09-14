from rest_framework import serializers


from .models import List, Card
#translates from python to JSON
#HyperlinkedModelSerializer
class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List

        fields = '__all__'

#Model.Serielizer
class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card

        fields = '__all__'


