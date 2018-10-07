from django.shortcuts import get_object_or_404

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantService:

    def retrieve(self, **kwargs):
        obj = get_object_or_404(Restaurant, **kwargs)
        serializer = RestaurantSerializer(obj)
        return serializer.data

    def get_list(self):
        data = Restaurant.objects.all()
        serializer = RestaurantSerializer(data, many=True)
        return {'results': serializer.data}

    def create(self, request):
        serializer = RestaurantSerializer(data=request)

        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None


