from production_line import ProductionLine
from production_order import ProductionOrder


class MES:
    def __init__(self):
        self.__production_lines: list[ProductionLine] = []
        self.production_orders: list[ProductionOrder] = []


    def add_production_line(self, name):
        self.__production_lines += ProductionLine(name)


    def get_production_line(self, name) -> ProductionLine:
        for line in self.__production_lines:
            if line.get_product_name() == name:
                return line
        return "not found"



    def create_production_order(self, production_line_name, order_number:int):
        self.production_orders.append(ProductionOrder(order_number))
        print("production order created")

    def start_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        production_line.start_order(order_number)
        print("production order started")


    def finish_production_order(self, production_line_name, order_number):
        production_line = self.get_production_line(production_line_name)
        production_line.finish_order(order_number)
        print("production order finished")


    