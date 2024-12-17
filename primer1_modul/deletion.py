import primer1_modul
import primer1_modul.showcase as showcase

def delete_a_car():
    showcase.show_cars()
    try:
        deletion_id = input("Enter the inventory ID for car you wish to delete: ")
        deletion_id = int(deletion_id)

        list_index = primer1_modul.find_for_inventory_id(deletion_id)
        if list_index > -1:
            cars = primer1_modul.load_cars()
            del cars[list_index]
            primer1_modul.save_cars(cars)
            print("The car has been successfully deleted.")
        else:
            print(f"There is no car with inventory ID: {deletion_id}")
    except ValueError:
        print(f"Can't convert '{deletion_id}' to whole number.")