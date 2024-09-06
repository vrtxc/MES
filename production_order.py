import time
import random

class ProductionOrder:
    def __init__(self, orderNumber, product_name, quantity):
        self.orderNumber = orderNumber
        self.productName = product_name
        self.quantity = quantity
        self.status = 'TODO'
        self.productionTime = 0
        self.finishedProduct = 0
        self.efficiency = 0
    
    def get_order_number(self):
        return self.orderNumber
    
    def start(self):
        self.status = 'RUNNING'
        print(f'Order {self.orderNumber} has started production of {self.productName}')
        self.produce(self.quantity)
        self.finish()
    
    def finish(self):
        self.status = 'DONE'
        print(f'Order {self.orderNumber} has finished')
        print(f'Efficiency of Order {self.orderNumber} was {self.get_production_efficiency()} units per second')
        return 
    
    def produce(self, units):
        for i in range (0, units):
            delay = random.randint(1, 2)
            time.sleep(delay)
            self.finishedProduct += 1
            print(f'{self.finishedProduct}  units of {units} in Order {self.orderNumber} have been completed')
            self.productionTime += delay
        return 
            
    def get_production_efficiency(self):
        self.efficiency =  self.finishedProduct  / self.productionTime
        return self.efficiency
    
    
ProductionOrder_1 = ProductionOrder(1, 'Robot', 4)
ProductionOrder_1.start()