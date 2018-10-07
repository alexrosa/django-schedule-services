from django_filters import rest_framework as filters

from reservation.models import Reservation

class ReservationFilter(filters.FilterSet):
    class Meta:
        model = Reservation
        fields={
            'reserved_date': ['exact', 'in'],
            'start_time': ['exact', 'in', 'gte', 'lte'],
            'end_time': ['exact', 'in', 'gte', 'lte']
        }