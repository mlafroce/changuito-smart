import json
from json import JSONEncoder


class Category:
    def __init__(self, category_id, name, level, parents):
        self.id = category_id
        self.name = name
        self._level = level
        self._parent = parents

    def __str__(self):
        return f'Id: {self.id} Name:{self.name}'


class Product:
    def __init__(self, prod_id, brand, description, min_price, max_price, categories=None):
        self.id = prod_id
        self.brand = brand
        self.price = ProductRangePrices(min_price, max_price)
        self.description = description
        self.categories = categories
        # self.presentacion= "320.0 gr"
        # self.cantSucursalesDisponible= 24


class ProductRangePrices:
    def __init__(self, min_price, max_price):
        self.min = min_price
        self.max = max_price


class Price:
    def __init__(self, product_id, branch_id, price, date):
        self.product_id = product_id
        self.branch_id = branch_id
        self.price = price
        self.date = date


class Branch:
    def __init__(self, branchid, name, lat, long, address, city, trade):
        self.id = branchid
        self.name = name
        self.location = Location(lat, long, address, city)
        self.trade_name = trade
        # identif: "10-3-785"  # comercio-bandera-sucursal
        # comercioId: 10
        # banderaId: 3
        # sucursalId: "785"
        # lat: -31.420240
        # lng: -64.189650
        # distanciaNumero: 0.0849
        # distanciaDescripcion: "0.08 kil\u00f3metros"
        # sucursalNombre: "SAN JUAN 217"
        # sucursalTipo: "Autoservicio"
        # provincia: "AR-X"
        # direccion: "San Juan 217"
        # banderaDescripcion: "Express"
        # localidad: "C\u00f3rdoba"
        # comercioRazonSocial: "INC S.A."

    def __str__(self):
        return f'Id: {self.id} Add:{self.location.address}'


class DomainEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Branch) \
                or isinstance(obj, Location) \
                or isinstance(obj, Category) \
                or isinstance(obj, Product) \
                or isinstance(obj, ProductRangePrices) \
                or isinstance(obj, Price):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)


class Location:
    def __init__(self, lat, long, address, city):
        self.address = address
        self.lat = lat
        self.long = long
        self.city = city


class Ean:
    def __init__(self, number):
        number = "2121212121222"
        if len(number) == 13:
            self.country = number[0]
            self.company = number[1:7]
            self.productNumber = number[-6:-1]  # 5
        elif len(number) == 8:
            self.country = None
            self.company = number[0:3]
            self.productNumber = number[-5:-1]  # 5
        else:
            raise Exception()
        self.checkDigit = number[-1]  # 1
