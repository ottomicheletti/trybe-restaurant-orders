class InventoryControl:
    def __init__(self):
        self.__ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }
        self.__minimum_stock = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.__total_ingredients = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self.__available_ingredients = list()
        self.__available_dishes = set()

    def add_new_order(self, _customer, order, _day):
        for item in self.__ingredients[order]:
            if self.__total_ingredients[item] < self.__minimum_stock[item]:
                self.__total_ingredients[item] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.__total_ingredients

    def get_available_dishes(self):
        for (key, value) in self.__total_ingredients.items():
            if value < self.__minimum_stock[key]:
                self.__available_ingredients.append(key)

        for (key, value) in self.__ingredients.items():
            if set(value).issubset(set(self.__available_ingredients)):
                self.__available_dishes.add(key)

        return self.__available_dishes
