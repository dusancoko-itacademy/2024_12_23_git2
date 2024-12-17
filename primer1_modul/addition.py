import primer1_modul
import primer1_modul.models as models

def add_new_car():
    print("--- New car addition ---")
    maker = input("Enter the car manufacturer: ")
    model = input("Enter the car model: ")
    year = input("Enter production year: ")

    cars = primer1_modul.load_cars()
    last_id = cars[len(cars)-1].inventory_id
    new_id = last_id + 1
    new_car = models.Car(new_id, maker, model, int(year))
    cars.append(new_car)
    primer1_modul.save_cars(cars)
    print(f"New car has been saved under ID: {new_id}")