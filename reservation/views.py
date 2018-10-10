import coreapi
import coreschema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas import AutoSchema

from reservation.services import ReservationService


class ReservationView(APIView):
    service_class = ReservationService

    def post(self, request, restaurant_id):
        """
        Create a new reservation
        """
        service = self.service_class()
        saved_obj = service.create(request.data, restaurant_id)
        if saved_obj:
            return Response(saved_obj, status=status.HTTP_201_CREATED)
        return Response("Internal Error", status.HTTP_400_BAD_REQUEST)

    def get(self, request, restaurant, id):
        service = self.service_class()
        if restaurant is None:
            return Response("You need to inform a restaurant ID", status.HTTP_400_BAD_REQUEST)

        result = service.retrieve(restaurant_id=restaurant,
                                  reservation_id=id)
        if result is not None:
            return Response(result, status.HTTP_200_OK)
        return Response("Internal error", status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant, id):
        service = self.service_class()
        if restaurant is None or id is None:
            return Response(status.HTTP_406_NOT_ACCEPTABLE)
        result = service.delete(restaurant, id)
        if result:
            return Response(status.HTTP_204_NO_CONTENT)
        else:
            return Response(status.HTTP_304_NOT_MODIFIED)


class ReservationListView(APIView):
    service_class = ReservationService

    def get(self, request, restaurant):
        service = self.service_class()
        result = service.get_list(request, restaurant_id=restaurant)
        if result:
            return Response(result, status.HTTP_200_OK)
        return Response(status.HTTP_204_NO_CONTENT)