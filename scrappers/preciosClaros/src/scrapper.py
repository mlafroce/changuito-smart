#!/usr/bin/env python3
import json
import logging

import requests

from .domainEntities import Category, Branch, Product, DomainEncoder

AGENT_USER = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
BRANCH_PARAMS_LIMIT = 30
PRODUCT_PARAMS_LIMIT = 100


class BaseScrapper:
    def __init__(self, dataProcessorHost):
        self.url = "https://d3e6htiiul5ek9.cloudfront.net"
        self.categories_endpoint = "/prod/categorias"  # Los par\u00e1metros permitidos en esta consulta son: lat, lng, cant_sucursales, count, array_sucursales.
        self.products_endpoint = "/prod/productos"
        self.sucursales = "/prod/sucursales"
        self.dataProcessorHost = dataProcessorHost
        self.endpoints = {
            "branches": "/branches"
        }

    def _brachesRequest(self, offset=0):
        return requests.get(self.url + self.sucursales,
                            params={"limit": BRANCH_PARAMS_LIMIT,
                                    "offset": offset},
                            headers={'User-Agent': AGENT_USER}
                            ).json()

    def supermarket_branches(self, all=True):
        # Los parametros permitidos en esta consulta son:
        # lat, lng, limit, offset, sucursal_provincia, sucursal_tipo,
        # comercio_bandera_nombre, comercio_razon_social, distancia_min, distancia_max, entorno.
        logging.info(f'Getting branches...')
        response = self._brachesRequest()
        branches = self._toBranches(response["sucursales"])
        if not all:
            return branches
        currentOffset = BRANCH_PARAMS_LIMIT
        while len(branches) < response["total"] and len(branches) == currentOffset:
            response = self._brachesRequest(currentOffset)
            branches += self._toBranches(response["sucursales"])
            currentOffset += BRANCH_PARAMS_LIMIT
        logging.info(f'>>> {len(branches)} banches were found')
        return branches

    def scrap_branches(self):
        data = self.supermarket_branches()
        url = f"{self.dataProcessorHost}{self.endpoints['branches']}"
        response = requests.post(url, json=json.dumps(data, cls=DomainEncoder))
        logging.info(response.json())

    def send_data(self):
        data = self.supermarket_branches()
        # logging.info(json.dumps(data, cls=DomainEncoder))
        url = f"{self.dataProcessorHost}{self.endpoints['branches']}"
        response = requests.post(url, json=json.dumps(data, cls=DomainEncoder))
        logging.info(response.json())

    def scrap(self):
        branches = self.supermarket_branches()
        productsByBranch = []
        it = 0
        for branch in branches:
            logging.info(
                f'[{branch.id}]>> {it}/{len(branches)}  Getting products for {branch.name} {branch.trade_name}')
            it += 1
            response = self._productByBrachRequest(branch.id)
            productsByBranch += self._toProducts(response["productos"], branch)
            currentOffset = PRODUCT_PARAMS_LIMIT
            while len(productsByBranch) == currentOffset:
                logging.info(f'[{branch.id}]>>>> Prod it {len(response["productos"])}/{response["total"]}  ')
                response = self._productByBrachRequest(branch.id, currentOffset)
                productsByBranch += self._toProducts(response["productos"], branch)
                currentOffset += BRANCH_PARAMS_LIMIT
            logging.info(f'[{branch.id}]>>>> TOTAL BY BRANCH {len(productsByBranch)} products were found')
        logging.info(f' TOTAL PRODUCTS {len(productsByBranch)} ')
        return productsByBranch

    def _productByBrachRequest(self, id_branch, offset=0):
        return requests.get(self.url + self.products_endpoint,
                            params={"limit": PRODUCT_PARAMS_LIMIT,
                                    "offset": offset,
                                    "id_sucursal": id_branch},
                            headers={'User-Agent': AGENT_USER}
                            ).json()

    def _toProducts(self, json_product_list, branch):
        return list(map(lambda x: Product(x["id"], x["marca"],
                                          x["precioMin"], x["precioMax"], x["precio"],
                                          x["nombre"], branch), json_product_list))

    def _toBranches(self, json_branch_list):
        return list(map(lambda x: Branch(x["id"], x["sucursalNombre"],
                                         x["lat"], x["lng"], x["direccion"], x["localidad"],
                                         x["comercioRazonSocial"]),
                        json_branch_list))



    def get_products(self):
        product_endpoint = self.url + '/todos/1'
        response = requests.get(product_endpoint)
        logging.info(response.json())

    def first_level_categories(self):
        # no pude encontrar un filtro para hacerlo directamente en la request
        response = requests.get(self.url + self.categories_endpoint, headers={'User-Agent': AGENT_USER}).json()
        # response format
        # {
        #     "status": 200,
        #     "totalPagina": 2286,
        #     "categorias": [ {
        #          "nivel":4,
        #          "categoriaRequerida":True,
        #          "nombre":"null",
        #          "productos":40,
        #          "identif":"061001001",
        #          "padres":[
        #             "FRESCOS",
        #             "COMIDAS ELABORADAS",
        #             "Rotiser\u00eda"
        #          ]
        #      }
        #     "total": 555,
        #     "maxCantSucursalesPermitido": 50
        # }
        firstLevelCategories = filter(lambda x: (x["nivel"] == 1), response["categorias"])
        # mappedCategories = []
        # for x in list(firstLevelCategories):
        #     currentCategory = Category(x["id"], x["nombre"])
        #     logging.info(currentCategory)
        #     mappedCategories.append(currentCategory)
        mappedCategories = list(map(lambda x: Category(x["id"], x["nombre"]), list(firstLevelCategories)))
        logging.info(f'{len(mappedCategories)} first level categories were found')
        return list(mappedCategories)

    def scrap_products(self):
        branches = self.supermarket_branches()
        productsByBranch = []
        it = 0
        for branch in branches:
            it += 1
            response = self._productByBrachRequest(branch.id)
            productsByBranch += self._toProducts(response["productos"], branch)
            currentOffset = PRODUCT_PARAMS_LIMIT
            while len(productsByBranch) == currentOffset:
                response = self._productByBrachRequest(branch.id, currentOffset)
                productsByBranch += self._toProducts(response["productos"], branch)
                currentOffset += BRANCH_PARAMS_LIMIT
            logging.info(
                f'{it}/{len(branches)} Brunch {branch.id} {branch.name} {branch.trade_name} has {len(productsByBranch)} products')
        return productsByBranch
