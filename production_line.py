from production_order import ProductionOrder

class ProductionLine:
    
    def __init__(self, name: str):
        self.__name: str = name
        self.__orders: list[ProductionOrder] = []
    

    def add_order(self, order_number: int, product_name: str, quantity: int):
        self.__orders.append(
            ProductionOrder(order_number, product_name, quantity)
        )


    def get_production_line_name(self) -> str:
        return self.__name
    

    def get_orders(self) -> list:
        return self.__orders


    def start_order(self, order_number: int):
        order = self.get_order_by_order_number(order_number)

        if not order:
            return
        
        order.start()


    def finish_order(self, order_number: int):
        order = self.get_order_by_order_number(order_number)

        if not order:
            return
        
        order.finish()
    

    def get_order_by_order_number(self, order_number: int) -> ProductionOrder:
        for order in self.__orders:
            if order.get_order_number() == order_number:
                return order