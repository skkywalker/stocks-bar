from flask import Flask, jsonify
from StocksBar.product import product
import threading
import logging

class bar_server:
    def __init__(self):
        self.products = []
        logging.info("Server initialized...")

    def run(self, h="localhost", p="5555", d=False, name="StocksBar"):
        if(len(self.products) == 0):
            logging.error("Trying to initialize with no products.")
            raise RuntimeError

        self.decrease_price_all()
        app = Flask(name)

        @app.route('/list')
        def list_products():
            return jsonify({i: str(p) for i, p in enumerate(self.products)})

        @app.route('/price/<product>')
        def consult_price(product):
            raise NotImplemented

        @app.route('/sell/<product>')
        def sell(product):
            raise NotImplemented

        app.run(host=h, port=p, debug=d)
        
    def add_product(self, p):
        logging.info(f"Adding product: {p.name}")
        if(not isinstance(p, product)):
            logging.error("Wrong type of variable when adding product")
            raise TypeError
        self.products.append(p)

    def add_products_from_db(self, location):
        raise NotImplemented

    def decrease_price_all(self):
        logging.info("Increasing prices...")
        for p in self.products:
            p.decrease_price()

        threading.Timer(5, self.decrease_price_all).start()
