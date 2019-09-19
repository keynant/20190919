import requests
import json


class Order:
    min_price = 100
    count = 0
    max_order = 0

    def __init__(self, product, price):
        Order.count +=1
        self.id = Order.count
        self.product = product
        self.__price = price
        self.changeMax()

    @classmethod
    def updateMinPrice(cls, new_min_price):
        cls.min_price = new_min_price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price
        self.changeMax()

    @staticmethod
    def from_string(fromstring):
        a = fromstring.split()
        return Order(a[0],int(a[1]))

    @staticmethod
    def from_dict(d):
        return Order(d['product'],int(d['price']))

    @classmethod
    def getCount(cls):
        return cls.count

    def aboveMinimum(self):
        return self.price - Order.min_price

    def changeMax(self):
        if self.price>Order.max_order:
            Order.max_order = self.price

    def __str__(self):
        result = ""
        for k,v in self.__dict__.items():
            if k == "_Order__price":
                result+= f'price - {v}\n'
            else:
                result+= f'{k} - {v}\n'
        result += 'Order count: '+str(self.getCount())+'\n'
        result += 'Maximum Order: '+str(self.max_order)+'\n'
        result += 'Current order above min: '+str(self.aboveMinimum())+'\n'
        return result


class Photo:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f'{k} - {v}\n'
        return result

    @staticmethod
    def from_web(url):
        resp = requests.get(url)
        if resp.status_code == 404:
            return "No picture at that ID"
        d=json.loads(resp.content)
        return Photo(d['id'], d['title'])







def main():
    order_1=Order.from_string("phone 200")
    print(order_1)
    d={"product" : 'laptop' , 'price' : 12000}
    Order.updateMinPrice(300)
    order_2=Order.from_dict(d)
    print(order_2)
    print(order_1)
    print(order_2.aboveMinimum())
    print(Order.count)
    print(Order.max_order)
    order_2.price = 2000000
    print(Order.max_order)
    print(Order.count)
    print(order_2)

    photo_1 = Photo.from_web('http://jsonplaceholder.typicode.com/photos/1')
    print(photo_1)



if __name__ == "__main__":
    main()
