from flask import Flask, request


# class GenericHandler:
#     def __init__(self, handle, method):
#         self.handle = handle
#         self.method = method
#
#     def __call__(self, *args):
#         try:
#             data = self.handle(args)
#             if data:
#                 return Response(response=data, status=200, headers={})
#             return Response(status=200, headers={})
#         except:
#             return Response(status=400)


class Server:
    def __init__(self, host, port, db_client=None):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.db_client = db_client
        # logging.info(f'{host}, {port}')
        self.set_routes()

    # def route(self, endpoint, handler, methods=['GET']):
    #     self.app.add_url_rule(endpoint, methods=methods, GenericHandler(handler.handle, methods[0]))

    def set_routes(self):
        try:
            self.app.add_url_rule('/products', view_func=self._handle_post, methods=['POST'])
            self.app.add_url_rule('/', view_func=self._handle_post, methods=['POST'])
        except Exception as error:
            print(error)

    def _handle_post(self):
        data = request.get_json()
        response = self.db_client.add(data)
        return response

    def close(self):
        pass

    def run(self):
        self.app.run(host=self.host, port=self.port)
