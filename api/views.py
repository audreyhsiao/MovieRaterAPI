from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import  Response
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = (MovieSerializer)
    
    # self-define method 
    @action(detail=True, methods=['POST']) #tell the frame work what method this will be
    # detail true means on a specific movie and detail false means on the list of movies
    def rate_movie(self, request, pk=None): # pk stands for primary key
        if 'stars' in request.data:
            response = {'message':"it's working"}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':"you need to provide your rating on a movie!"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer)