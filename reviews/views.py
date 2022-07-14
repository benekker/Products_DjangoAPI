
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .variable_constants import GET, POST, PUT, DELETE


@api_view([GET, POST])
def review_list(request, pk):

    if request.method == GET:
        reviews = Review.objects.filter(product_id = pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == POST:
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view([GET, PUT, DELETE])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == GET:
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == PUT:
        serializer = ReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == DELETE:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)