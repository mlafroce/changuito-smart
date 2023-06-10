import json
import logging

import pymongo
from flask import Flask, request


# class GenericHandler:
#     def __init__(self, handle, method):
#         self.handle = handle
#         self.method = method
#
#     def __call__(self, *args):
#         try:
#             datavieja = self.handle(args)
#             if datavieja:
#                 return Response(response=datavieja, status=200, headers={})
#             return Response(status=200, headers={})
#         except:
#             return Response(status=400)


class Server:
    def __init__(self, host, port, domain_manager=None):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.domain_manager = domain_manager
        self.set_routes()

    # def route(self, endpoint, handler, methods=['GET']):
    #     self.app.add_url_rule(endpoint, methods=methods, GenericHandler(handler.handle, methods[0]))

    def set_routes(self):
        try:
            self.app.add_url_rule('/health', view_func=self._handle_post, methods=['GET'])
            self.app.add_url_rule('/products', view_func=self._handle_post, methods=['POST'])
            self.app.add_url_rule('/', view_func=self._handle_post, methods=['POST'])
            self.app.add_url_rule('/branches', view_func=self._handle_post_branches, methods=['POST'])
            self.app.add_url_rule('/categories', view_func=self._handle_post_categories, methods=['POST'])
            self.app.add_url_rule('/product', view_func=self._handle_post_product, methods=['POST'])
            self.app.add_url_rule('/price', view_func=self._handle_post_price, methods=['POST'])
        except Exception as error:
            print(error)
            logging.error("Could not set routes")

    def _handle_post(self):
        data = request.get_json()
        response = self.domain_manager.add(data)
        return response

    def _handle_post_branches(self):
        try:
            data = request.get_json()
            # validate branches schema
            # branches = map(lambda x: (Branch(x)), datavieja)
            response = self.domain_manager.add_branches(json.loads(data))
            logging.info(f"Branches ids inserted {len(response)}")
            return {"inserted": len(response)}
        except pymongo.errors.BulkWriteError as error:
            return {"inserted": 0}

    def _handle_post_categories(self):
        try:
            data = request.get_json()
            response = self.domain_manager.add_categories(json.loads(data))
            logging.info(f"Categories ids inserted {len(response)}")
            return {"inserted": len(response)}
        except pymongo.errors.BulkWriteError as error:
            return {"inserted": 0}

    def _handle_post_product(self):
        try:
            data = request.get_json()
            response = self.domain_manager.add_product(json.loads(data))
            return {"inserted": len(response)}
        except pymongo.errors.BulkWriteError as error:
            return {"inserted": 0}

    def _handle_post_price(self):
        try:
            data = request.get_json()
            response = self.domain_manager.add_price(json.loads(data))
            return {"inserted": len(response)}
        except pymongo.errors.BulkWriteError as error:
            return {"inserted": 0}

    def close(self):
        pass

    def run(self):
        self.app.run(host=self.host, port=self.port)
