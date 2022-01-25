from typing import List, Union
from datetime import datetime

class Fish:
    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime("21/01/2022")
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100

class FishShop:
    def add_fish(self, fish_name: str, total_weight: float) -> None:
        pass
    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        pass
    def sell_fish(self, fish_name: str, weight: float) -> float:
        pass
    def cast_out_old_fish(self) -> List[Union[str, float]]:
        pass

class Seller:
    def evaluate_price(self, fish: List[Fish]) -> float:
        pass
    def sign_contract_with_shop(self, shop: FishShop) -> bool: # Gonna return True, if it was signed successfully or False otherwise
        pass
    def take_and_process_order(self, fish: List[Fish]) -> bool:
        pass
    def ask_if_fish_is_available_in_shop(self, order: List[Fish], shop: FishShop) -> bool:
        pass

class Buyer:
    def get_available_seller(self, shop: FishShop) -> Seller:
        pass
    def contact_seller(self, seller: Seller) -> bool:
        pass
    def create_order(self, shop: FishShop) -> List[Fish]:
        pass
    def send_order_to_seller(self, order: List[Fish], seller: Seller) -> bool: # Gonna return True, if it was sent successfully or False otherwise
        pass