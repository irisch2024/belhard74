#Написать класс Car

class Car:

    def __init__(self, color, count_passenger_seats, s_baby_seat):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.s_baby_seat = s_baby_seat
        self.is_busy = False


    def __str__(self):
        return f"color={self.color} count_passenger_seats={self.count_passenger_seats} s_baby_seat={self.s_baby_seat} is_busy={self.is_busy}"


Car1 = Car(color="Green", count_passenger_seats=4, s_baby_seat = True)
Car2 = Car(color="Red", count_passenger_seats=4, s_baby_seat = False)

print(Car2.s_baby_seat)
print(Car1)
print(Car2)
