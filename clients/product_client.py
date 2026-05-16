from clients.base_client import BaseClient

class ProductClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "products"

    def get_all_products(self):
        return self.get(self.endpoint)

    def get_product(self, product_id):
        return self.get(f"{self.endpoint}/{product_id}")

    def create_product(self, product_data):
        return self.post(self.endpoint, data=product_data)

    def update_product(self, product_id, product_data):
        return self.put(f"{self.endpoint}/{product_id}", data=product_data)

    def delete_product(self, product_id):
        return self.delete(f"{self.endpoint}/{product_id}")
