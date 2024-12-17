from pathlib import Path
import json  
import primer1_modul.models as models
from dataclasses import asdict 

class Configuration:
    CARS_PATH: Path = None 

    @classmethod
    def set_initial_path(cls, init_path: Path):
        if not init_path.exists():
            raise FileNotFoundError(f"File '{init_path.absolute}' doesn't exist.")
        cls.CARS_PATH = init_path

def load_cars() -> list[models.Car]:
    path = Configuration.CARS_PATH
    cars_dict_list = json.loads(path.read_text())
    cars: list[models.Car] = [models.Car(**c) for c in cars_dict_list]
    return cars 

def save_cars(cars : list[models.Car]):
    path = Configuration.CARS_PATH
    cars_dict_list = [ asdict(c) for c in cars ]
    path.write_text(json.dumps(cars_dict_list, indent=4))
    

def find_for_inventory_id(i_id: int):
    cars = load_cars()
    list_index = -1
    for i in range(len(cars)):
        if cars[i].inventory_id == i_id:
            list_index = i 
            break 
    return list_index
