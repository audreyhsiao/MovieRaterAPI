from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        #TODO hash the password or it will easily be seen by using GET method by un-authorized user
        extra_kwargs = {'password':{'write_only':True, 'required': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie # tell serializer what model we are using
        fields = ('id','title','description','num_of_ratings') # tell serializer which part we are using it
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','movie')