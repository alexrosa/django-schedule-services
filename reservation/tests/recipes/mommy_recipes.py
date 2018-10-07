from datetime import datetime, timedelta
from reservation.models import Reservation
from model_mommy.recipe import Recipe, seq, foreign_key
from restaurant.models import Restaurant

current_date = datetime.now()
now = format(datetime.now(), '%H:%M')
one_hour_more = format(datetime.now() + timedelta(hours=1), '%H:%M')

restaurant = Recipe(Restaurant, restaurant_id=seq(1),
                           name="rezzyraunt")

reservation = Recipe(Reservation,
                            restaurant=foreign_key(restaurant),
                            reservation_id=seq(1),
                            number_of_customers=3,
                            reserved_date=current_date,
                            status=1,
                            deposit=30,
                            start_time=now,
                            end_time=one_hour_more,
                            fee=0)