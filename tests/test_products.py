import pytest

@pytest.mark.api
@pytest.mark.regression
class TestProducts:
    """Standardized test suite for Products API."""

    @pytest.mark.smoke
    def test_get_all_products(self, product_client):
        """Verify that all products can be fetched successfully."""
        response = product_client.get_all_products()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    @pytest.mark.smoke
    def test_get_single_product(self, product_client):
        """Verify fetching a specific product by its ID."""
        product_id = 1
        response = product_client.get_product(product_id)
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == product_id
        assert 'title' in data

    def test_create_product(self, product_client, faker):
        """Verify creating a new product with dynamic data."""
        new_product = {
            "title": faker.word(),
            "price": float(faker.random_number(digits=2)),
            "description": faker.sentence(),
            "image": faker.image_url(),
            "category": faker.word()
        }
        response = product_client.create_product(new_product)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == new_product['title']
        assert 'id' in data

    def test_update_product(self, product_client, faker):
        """Verify updating an existing product's information."""
        product_id = 1
        updated_data = {
            "title": f"Updated {faker.word()}",
            "price": 99.99
        }
        response = product_client.update_product(product_id, updated_data)
        assert response.status_code == 200
        assert response.json()['title'] == updated_data['title']

    def test_delete_product(self, product_client):
        """Verify deleting a product."""
        product_id = 1
        response = product_client.delete_product(product_id)
        assert response.status_code == 200
        # Mock API returns the deleted object
        assert response.json()['id'] == product_id

    # --- Negative Test Cases ---

    def test_get_non_existent_product(self, product_client, faker):
        """Verify that fetching a non-existent product returns expected null/empty response."""
        product_id = faker.random_int(min=9999, max=99999)
        response = product_client.get_product(product_id)
        assert response.status_code == 200
        assert response.text == "" or response.json() is None

    def test_create_product_invalid_data(self, product_client):
        """Verify creation behavior when sending empty payload."""
        response = product_client.create_product({})
        assert response.status_code == 201
        assert 'id' in response.json()
