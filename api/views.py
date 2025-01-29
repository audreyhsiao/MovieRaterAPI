from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import  Response
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = (MovieSerializer)
    authentication_classes = (TokenAuthentication,)
    
    # self-define method 
    @action(detail=True, methods=['POST']) #tell the frame work what method this will be
    # detail true means on a specific movie and detail false means on the list of movies
    def rate_movie(self, request, pk=None): # pk stands for primary key
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            #user = User.objects.get(id=1)
            user = request.user
            print('user: ', user)
            # we have to check if the rating of this movie from this user does exist
            try:
                 rating = Rating.objects.get(user=user.id, movie=movie.id) #  there's a rating for this movie-rating relationship
                 rating.stars = stars # updating the rating for this movie from this user
                 rating.save()
                 serializer = RatingSerializer(rating, many=False)
                 response = {'message': 'Rating updated', 'result': serializer.data}
            except:
                # if no, create one
                Rating.objects.create(user=user, movie=movie, stars = stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                
                
            #response = {'message':"it's working"}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message':"you need to provide your rating on a movie!"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer)
    authentication_classes = (TokenAuthentication,)