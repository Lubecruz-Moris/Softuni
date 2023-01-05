from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __id_finder(self, entities, entity_id):
        for entity in entities:
            if entity_id == entity.id:
                return entity

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__id_finder(self.customers, customer_id)
        dvd = self.__id_finder(self.dvds, dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__id_finder(self.customers, customer_id)
        dvd = self.__id_finder(self.dvds, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def print_list(self, entities):
        result = ''
        for entity in entities:
            result += repr(entity) + '\n'
        return result

    def __repr__(self):
        result = self.print_list(self.customers)
        result += self.print_list(self.dvds)
        return result.strip()
