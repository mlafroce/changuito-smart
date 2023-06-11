#!/usr/bin/env python3
import json
import logging
from datetime import date

import requests

from .domainEntities import Product, Price, DomainEncoder, Branch, Category

AGENT_USER = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
BRANCH_PARAMS_LIMIT = 30
PRODUCT_PARAMS_LIMIT = 100


class BaseScrapper:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.url = kwargs.get("url", "https://d3e6htiiul5ek9.cloudfront.net")
        self.endpoint = kwargs.get("endpoint")
        self.dst_url = kwargs.get("dst_url")
        self.dst_endpoint = kwargs.get("dst_endpoint")
        self.enpoint_limit_result = kwargs.get("limit")
        self.domain = kwargs.get("domain")
        self.encoder = kwargs.get("domain_encoder")

    def scrap(self):
        logging.info(f'{self.name} - Scrapping starts...')
        currentOffset = 0
        current_data = []
        total_data = []
        while len(total_data) == currentOffset:
            response = self._get_data(limit=self.enpoint_limit_result, offset=currentOffset)
            current_data = self._map_to_domain(response)
            total_data += current_data
            response = self._send_data(current_data)
            currentOffset += self.enpoint_limit_result
            logging.info(f'{self.name} - Sending {len(current_data)}... getting {response.json()}')
        logging.info(f"{self.name} - Scrapping ends")
        return total_data

    def _get_data(self, **params):
        try:
            url = f"{self.url}{self.endpoint}"
            logging.info(f"Getting data from {url} with offset {params.get('offset', '-')}")
            print(requests.get(url,
                               params=params,
                               headers={'User-Agent': AGENT_USER}
                               ))
            return requests.get(url,
                                params=params,
                                headers={'User-Agent': AGENT_USER}
                                ).json()
        except Exception as error:
            logging.error(f"Something Wrong _get_data: {error}")

    def _send_data(self, data):
        dst_url = f"{self.dst_url}{self.dst_endpoint}"
        return requests.post(dst_url, json=json.dumps(data, cls=self.encoder))

    def _map_to_domain(self, json_data):
        pass


class BranchesScrapper(BaseScrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Los parametros permitidos en esta consulta de sucursales son:
        # lat, lng, limit, offset, sucursal_provincia, sucursal_tipo,
        # comercio_bandera_nombre, comercio_razon_social, distancia_min, distancia_max, entorno.

    def _map_to_domain(self, json_data):
        json_branch_list = json_data["sucursales"]
        return list(map(lambda x: self.domain(x["id"], x["sucursalNombre"],
                                              x["lat"], x["lng"], x["direccion"], x["localidad"],
                                              x["comercioRazonSocial"]),
                        json_branch_list))


class CategoriesScrapper(BaseScrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_data(self, **params):
        url = f"{self.url}{self.endpoint}"
        logging.info(f"Getting data from {url}")
        return requests.get(url, headers={'User-Agent': AGENT_USER}).json()

    def _map_parents(self, categories):
        categories_id_by_name = {}
        for category in categories:
            categories_id_by_name[category["nombre"]] = category["id"]
        for category in categories[1:3]:
            parents_id = [categories_id_by_name[x] for x in category["padres"]]
            category["padres"] = parents_id
        return categories

    def _map_to_domain(self, json_data):
        json_branch_list = self._map_parents(json_data["categorias"])
        return list(map(lambda x: self.domain(x["id"], x["nombre"],
                                              x["nivel"], x["padres"]),
                        json_branch_list))


class PriceScrapper:
    def __init__(self, **kwargs):
        self.name = "PRICE SCRAPPER"
        self.scrap_url = kwargs.get("scrap_url", "https://d3e6htiiul5ek9.cloudfront.net")
        self.scrap_endpoints = kwargs.get("scrap_endpoints")
        self.dst_url = kwargs.get("dst_url")
        self.dst_endpoints = kwargs.get("dst_endpoints")
        self.enpoint_limit_result = kwargs.get("limit")
        self.branch_scrapper = BranchesScrapper(dst_url=self.dst_url,
                                                dst_endpoint=self.dst_endpoints["branches"],
                                                url=self.scrap_url, endpoint=self.scrap_endpoints["branches"],
                                                limit=100,
                                                domain=Branch, domain_encoder=DomainEncoder, name="BRANCH SCRAPPER"
                                                )
        self.categories_scrapper = CategoriesScrapper(dst_url=self.dst_url,
                                                      dst_endpoint=self.dst_endpoints["categories"],
                                                      url=self.scrap_url, endpoint=self.scrap_endpoints["categories"],
                                                      limit=30,
                                                      domain=Category, domain_encoder=DomainEncoder,
                                                      name="CATEGORY SCRAPPER"
                                                      )

    def _map_products(self, json_data):
        json_list = json_data["productos"]
        return list(map(lambda x: Product(x["id"], x["marca"], x["nombre"], x["precioMin"], x["precioMax"]), json_list))

    def _map_prices(self, json_data, branch_id=None):
        json_list = json_data["productos"]
        return list(map(lambda x: Price(x["id"], branch_id, x["precio"], str(date.today())), json_list))

    def _send_products(self, data):
        try:
            dst_url = f"{self.dst_url}{self.dst_endpoints['products']}"
            response = requests.post(dst_url, json=json.dumps(data, cls=DomainEncoder))
            return response.json()
        except Exception as error:
            logging.error(f"Something Wrong _send_products: {error}")

    def _send_prices(self, data):
        try:
            dst_url = f"{self.dst_url}{self.dst_endpoints['prices']}"
            response = requests.post(dst_url, json=json.dumps(data, cls=DomainEncoder))
            return response.json()
        except Exception as error:
            logging.error(f"Something Wrong _send_prices: {error}")

    def _get_data(self, **params):
        try:
            url = f"{self.scrap_url}{self.scrap_endpoints['products']}"
            logging.info(f"Getting data from {url}  offset {params.get('offset')}")
            return requests.get(url, params=params, headers={'User-Agent': AGENT_USER}).json()
        except Exception as error:
            logging.error(f"Something Wrong _get_data: {error}")

    def scrap(self):
        logging.info(f'{self.name} - Scrapping starts...')
        branches = self.branch_scrapper.scrap()
        for branch in branches:
            logging.info(f'{self.name} - Scrapping starts by branch {branch.name} {branch.trade_name}...')
            current_products, current_prices = self._scrap_by_branch(branch.id)
            if len(current_products) == 0 or len(current_prices) == 0:
                logging.info(f'{self.name} - Scrapping ends by branch {branch.name} {branch.trade_name}...')
                continue
            response_prod = self._send_products(current_products)
            logging.info(f'{self.name} - Sending products {len(current_products)}... getting {response_prod}')
            response_pric = self._send_prices(current_prices)
            logging.info(f'{self.name} - Sending prices {len(current_prices)}... getting {response_pric}')
            logging.info(f'{self.name} - Scrapping ends by branch {branch.name} {branch.trade_name}...')
        logging.info(f'{self.name} - Scrapping ends...')

    def _scrap_by_branch(self, branch_id):
        currentOffset = 0
        total_products = []
        total_prices = []
        while len(total_products) == currentOffset:
            response = self._get_data(limit=self.enpoint_limit_result, offset=currentOffset, id_sucursal=branch_id)
            total_products += self._map_products(response)
            total_prices += self._map_prices(response, branch_id)
            currentOffset += self.enpoint_limit_result
        return total_products, total_prices
