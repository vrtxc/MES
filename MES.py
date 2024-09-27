from production_line import ProductionLine
from production_order import ProductionOrder


class MES:
    def __init__(self):
        self.__production_lines: list[ProductionLine] = []


    def add_production_line(self, name: str):
        if not isinstance(name, str) or len(name) < 1:
            return print("Errr: invalid name")
        
        self.__production_lines.append(ProductionLine(name))
        print(f"production line {name} added")


    def get_production_line(self, name: str) -> ProductionLine:
        for line in self.__production_lines:
            if line.get_product_name() == name:
                return line
        return "not found"



    def create_production_order(self, production_line_name: str, order_number: int, product_name: str, quantity: int):
        production_line = self.get_production_line(production_line_name)

        if production_line == "not found":
            return print("Error: production line not found")
        
        if quantity < 1:
            return print("Errr: quantity needs to be at least 1")
        
        production_line.add_order(order_number, product_name, quantity)        
        print("production order created")

    def start_production_order(self, production_line_name: str, order_number: int):
        production_line = self.get_production_line(production_line_name)

        if production_line == "not found":
            return print("Error: production line not found")
        
        production_line.start_order(order_number)
        print("production order started")


    def finish_production_order(self, production_line_name: str, order_number: int):
        production_line = self.get_production_line(production_line_name)

        if production_line == "not found":
            return print("Error: production line not found")
        
        production_line.finish_order(order_number)
        print("production order finished")


    