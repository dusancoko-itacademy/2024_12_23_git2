from dataclasses import dataclass

@dataclass
class Car:
    inventory_id: int 
    car_maker: str 
    car_model: str 
    car_year: int 