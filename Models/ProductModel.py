class ProductModel:

    def __init__(self):
        self.product_db = dict()

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.product_db[product_name] = {"product_name": product_name, 
                                         "product_type": product_type, 
                                         "available_quantity": available_quantity, 
                                         "unit_price": unit_price
                                        }
        return True

    def search_product(self, product_name):
        if (product_name in self.product_db):
            print("\nSearched Product Details:")
            for key in self.product_db[product_name]:
                print(key + ':', self.product_db[product_name][key])
            return True
        else:
            return None

    def all_products(self):
        print("\n\nAll Product Details:")
        for product, details in self.product_db.items():
            print("\nProduct: ", product)
            for key in details:
                print(key + ':', details[key])
        return True

