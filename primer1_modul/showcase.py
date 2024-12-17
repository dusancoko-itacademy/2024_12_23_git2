from tabulate import tabulate
import primer1_modul

def show_cars():
    cars = primer1_modul.load_cars()
    print("--- Available cars ---")
    print(tabulate(cars, ["Inventory ID", "Maker", "Model", "Production Year"],
                   tablefmt="github"))