
class ProductionLine:
    
    def __init__(self, name):
        self.__name: str = name
        self.__order_number: int
        self.__product_name: str
        self.__quantity: int
    

    def create_order(self, order_number, product_name, quantity):
        pass


    def start_order(self, order_number):
        pass


    def finish_order(self, order_number):
        pass


    def get_name(self):
        return self.__name
    
    def get_order_number(self):
        return self.__order_number
    
    def get_product_name(self):
        return self.__product_name
    
    def get_quantity(self):
        return self.__quantity