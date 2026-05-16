import pytest

@pytest.mark.api
@pytest.mark.regression
class TestProducts:
    """Robust test suite using JSONPlaceholder for stable CI/CD execution."""

    @pytest.mark.smoke
    def test_get_all_products(self, product_client):
        """Verify fetching all posts."""
        response = product_client.get_all_products()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    @pytest.mark.smoke
    def test_get_single_product(self, product_client):
        """Verify fetching a specific post."""
        product_id = 1
        response = product_client.get_product(product_id)
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == product_id
        assert 'title' in data

    def test_create_product(self, product_client, faker):
        """Verify creating a new post."""
        payload = {
            "title": faker.sentence(),
            "body": faker.text(),
            "userId": 1
        }
        response = product_client.create_product(payload)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == payload['title']
        assert 'id' in data

    def test_update_product(self, product_client, faker):
        """Verify updating a post."""
        product_id = 1
        updated_data = {
            "title": "Updated Title",
            "body": faker.text(),
            "userId": 1
        }
        response = product_client.update_product(product_id, updated_data)
        assert response.status_code == 200
        assert response.json()['title'] == "Updated Title"

    def test_delete_product(self, product_client):
        """Verify deleting a post."""
        product_id = 1
        response = product_client.delete_product(product_id)
        assert response.status_code == 200

    # --- Negative Test Cases ---

    def test_get_non_existent_product(self, product_client, faker):
        """Verify 404 for non-existent post."""
        product_id = faker.random_int(min=9999, max=99999)
        response = product_client.get_product(product_id)
        assert response.status_code == 404

    def test_create_product_invalid_data(self, product_client):
        """Verify creation behavior with empty data."""
        response = product_client.create_product({})
        assert response.status_code == 201
        assert 'id' in response.json()
