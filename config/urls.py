from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework_swagger.views import get_swagger_view

from restaurant.views import RestaurantView, RestaurantViewList
from reservation.views import ReservationView, ReservationListView
schema_view = get_swagger_view(title='RezzyRaunt API')

urlpatterns = [
    path('', RedirectView.as_view(url='docs/')),
    path('docs/', schema_view),
    path('restaurant/<int:restaurant>/', RestaurantView.as_view(), name='restaurant'),
    path('restaurant-list/', RestaurantViewList.as_view(), name='restaurant-list'),
    path('reservation/<int:restaurant>/<int:id>/', ReservationView.as_view(), name='reservation'),
    path('reservation-list/<int:restaurant>/', ReservationListView.as_view(), name='reservation-list'),
]
