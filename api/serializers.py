from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie # tell serializer what model we are using
        fields = ('id','title','description','num_of_ratings') # tell serializer which part we are using it
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','movie')