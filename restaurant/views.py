from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from restaurant.services import RestaurantService


class RestaurantView(APIView):
    service_class = RestaurantService

    def get(self, request, restaurant):
        """
        Get a restaurant
        """
        service = self.service_class()
        result = service.retrieve(restaurant_id=restaurant)
        return Response(result)

    def post(self, request):
        """
        Create a new restaurant
        """
        service_class = RestaurantService()
        saved_obj = service_class.create(request.data)
        if saved_obj:
            return Response(saved_obj, status=status.HTTP_201_CREATED)

        return Response("Internal Error", status.HTTP_400_BAD_REQUEST)


class RestaurantViewList(APIView):

    def get(self, request):
        """
        Lsit all restaurants
        """
        service_class = RestaurantService()
        result = service_class.get_list()
        return Response(result, status.HTTP_200_OK)
