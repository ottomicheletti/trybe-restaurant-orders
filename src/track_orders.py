from statistics import mode


class TrackOrders:
    def __init__(self):
        self.__orders = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        self.__orders.append([customer, order, day])
        return self.__len__()

    def get_most_ordered_dish_per_customer(self, customer):
        return mode(
            [order[1] for order in self.__orders if order[0] == customer]
        )

    def get_never_ordered_per_customer(self, customer):
        return set(
            [order[1] for order in self.__orders]
        ).difference(set(
            [order[1] for order in self.__orders if order[0] == customer]
        ))

    def get_days_never_visited_per_customer(self, customer):
        return set(
            [order[2] for order in self.__orders]
        ).difference(set(
            [order[2] for order in self.__orders if order[0] == customer]
        ))

    def get_busiest_day(self):
        return mode([order[2] for order in self.__orders])

    def get_least_busy_day(self):
        pass
