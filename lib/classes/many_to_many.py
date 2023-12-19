import ipdb

class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        self.orderlist = []
        self.customerlist = []
        Coffee.all.append(self)

    def add_order(self, order):
        if isinstance(order, Order):
            self.orderlist.append(order)

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            if not customer in self.customerlist:
                self.customerlist.append(customer)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str):
            print("that is not a string")
        elif not len(name) >= 3:
            print("name too short")
        elif hasattr(self, "name"):
            print("you cannot change the name of coffee instances")
        else:
            self._name = name

    name = property(get_name, set_name)
        
    def orders(self):
        return self.orderlist
    
    def customers(self):
        return self.customerlist
    
    def num_orders(self):
        return len(self.orderlist)
    
    def average_price(self):
        return (sum([order.price for order in self.orderlist]))/(len(self.orderlist))

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        self.orderlist = []
        self.coffeelist = []
        Customer.all.append(self)

    def add_order(self, order):
        if isinstance(order, Order):
            self.orderlist.append(order)

    def add_coffee(self, coffee):
        if isinstance(coffee, Coffee):
            if not coffee in self.coffeelist:
                self.coffeelist.append(coffee)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            if len(name) >= 1 and len(name) <= 15:
                self._name = name
        else:
            print("that is not a string ")

    name = property(get_name, set_name)
        
    def orders(self):
        return self.orderlist
    
    def coffees(self):
        return self.coffeelist
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        # Order.all.append(new_order)
        return new_order
    
    def most_aficionado(coffee):
        # return the customer object who has spent the most money on the coffee object
        most_aficionado = None
        most_spent = 0
        # iterate through customers
        for cus in Customer.all:
            # how much did this customer spend?
            spent = sum([order.price for order in cus.orders() if order.coffee == coffee])
            # is this more than previous customers spent?
            if spent > most_spent:
                most_spent = spent
                most_aficionado = cus

        return most_aficionado
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.customer.add_order(self)
        self.customer.add_coffee(coffee)
        self.coffee.add_order(self)
        self.coffee.add_customer(customer)
        Order.all.append(self)

    def get_price(self):
        return self._price
        
    def set_price(self, price):
        if not hasattr(self, "price"):
            if isinstance(price, float):
                self._price = price

    price = property(get_price, set_price)



# ipdb.set_trace()