from datetime import datetime

#
from tools import *
#

class FishInfo:
    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, catch_date: datetime, due_time: datetime) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.catch_date = catch_date
        self.due_time = due_time

class Fish(FishInfo):
    def set_age_and_weight(self, age_in_months: int, weight: float) -> None:
        self.age_in_months = age_in_months
        self.weight = weight

class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, width: float, length: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.is_alive = is_alive

class FishShop:
    def __init__(self) -> None:
        fish_boxes = {} # Dict[str: list[FishBox]]
        fresh_fish = {} # Dict[str: list[Fish]]

    def add_fish(self, fish_box: FishBox) -> None:
        name = fish_box.fish_info.name
        if self.fish_boxes[name] == None:
            self.fish_boxes[name] = []
        self.fish_boxes[name].append(fish_box)

    def add_fish(self, fish: Fish) -> None:
        name = Fish.name
        if self.fresh_fish[name] == None:
            self.fresh_fish[name] = []
        self.fresh_fish[name].append(fish)

    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> bool: # Gonna return True if sold successfully or False otherwise
        lst = []
        if is_fresh:
            lst = self.fresh_fish[name]
        else:
            lst = self.fish_boxes[name]
        if lst == None or lst == [] or weight <= 0: return False
        total_weight = 0
        for i in lst:
            total_weight += i.weight
        if total_weight < weight: return False
        lst = Functions.sorted_by_function(lst, lambda x, y: (x.weight < y.weight))
        while weight > 0:
            l, r = 0, len(lst)-1
            while l<r:
                m = (l+r) >> 1
                if lst[m].weight >= weight:
                    r = m
                else:
                    l = m+1
            weight -= lst[r].weight
            del lst[r]
        if is_fresh:
            self.fresh_fish[name] = lst
        else:
            self.fish_boxes[name] = lst
        return True

    def get_fish_names_sorted_by_price(self) -> List[Union[str, bool, float]]:
        lst = []
        for key in self.fish_boxes.keys():
            lst.append([key, False, self.fish_boxes[key][0].fish_info.price_in_uah_per_kilo])
        for key in self.fresh_fish.keys():
            lst.append([key, True, self.fresh_fish[key][0].price_in_uah_per_kilo])
        return Functions.sorted_by_function(lst, lambda x, y: (x[2] < y[2]))

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