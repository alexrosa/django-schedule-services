from django.shortcuts import get_object_or_404

from reservation.serializers import ReservationSerializer
from reservation.models import Reservation
from reservation.filters import ReservationFilter


class ReservationService:
    serializer_class = ReservationSerializer

    def retrieve(self, **kwargs):
        obj = get_object_or_404(Reservation, **kwargs)
        serializer = self.serializer_class(obj)
        return serializer.data

    def get_list(self, request, restaurant_id):
        _filter = ReservationFilter(
            request.GET, queryset=Reservation.objects.filter(restaurant_id=restaurant_id)
        )
        serializer = self.serializer_class(_filter.qs, many=True)
        return {'results': serializer.data}

    def create(self, request):
        serializer = self.serializer_class(request)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None

    def delete(self, restaurant_id, reservation_id):
        obj = Reservation.objects.filter(restaurant__reservation=restaurant_id,
                                         reservation_id=reservation_id)
        if obj is not None:
            obj.delete()
            return True
        return False
