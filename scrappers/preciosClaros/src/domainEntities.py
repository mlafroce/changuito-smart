class Category(object):
    def __init__(self, id, name, level=1, req=True, parents=None):
        print(id, name)
        self.id = id
        self.name = name
        self._level = level
        self._required = req
        self._parent = parents

    def __str__(self):
        return f'Id: {self.id} Name:{self.name}'


class Product:
    def __init__(self, id, brand, minPrice, maxPrice, currentPrice, description, branch=None, categories=None):
        self.id = id
        self.brand = brand
        self.price = ProductPrice(minPrice, maxPrice, currentPrice)
        self.description = description
        self.branch = branch
        self.categories = categories
        # self.presentacion= "320.0 gr"
        # self.cantSucursalesDisponible= 24


class ProductPrice:
    def __init__(self, min, max, current):
        self.min = min
        self.max = max
        self.current = current


class Branch:
    def __init__(self, id, name, lat, long, address, city, trade):
        self.id = id
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
