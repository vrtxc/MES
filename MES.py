from production_line import ProductionLine

class MES:
    def __init__(self):
        self.__production_lines: list[ProductionLine] = []


    def add_production_line(self, name):
        self.__production_lines += ProductionLine(name)


    def get_production_line(self, name) -> ProductionLine:
        for line in self.__production_lines:
            if line.get_product_name() == name:
                return line

        return "not found"



    def create_production_order(self, production_line_name, order_number, product_name, quantity):
        production_line = self.get_production_line(production_line_name)
        production_line.create_order(order_number, product_name, quantity)


    def start_production_order(self, production_line_name, order_number):
        pass


    def finish_production_order(self, production_line_name, order_number):
        pass


    