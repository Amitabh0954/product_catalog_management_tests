import pytest
from unittest.mock import MagicMock
from backend.services.product.product_service import ProductService
from backend.models.product.product import Product

# Fixtures for mock repository
@pytest.fixture
def mock_product_repository():
    return MagicMock()

@pytest.fixture
def product_service(mock_product_repository):
    return ProductService(mock_product_repository)

# Test for add_new_product method

def test_add_new_product(product_service, mock_product_repository):
    mock_product_repository.get_product_by_name = MagicMock(return_value=None)
    mock_product_repository.add_product = MagicMock()
    product = product_service.add_new_product("Test Product", "This is a test product", 10.0)
    mock_product_repository.add_product.assert_called_once_with(product)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 10.0

# Test for add_new_product method with existing product name

def test_add_new_product_with_existing_name(product_service, mock_product_repository):
    mock_product_repository.get_product_by_name = MagicMock(return_value=Product(1, "Test Product", "This is a test product", 10.0))
    with pytest.raises(ValueError, match="Product with this name already exists"):
        product_service.add_new_product("Test Product", "This is a test product", 10.0)

# Test for update_product method

def test_update_product(product_service, mock_product_repository):
    product = Product(1, "Old Product", "Old description", 5.0)
    mock_product_repository.get_product_by_id = MagicMock(return_value=product)
    mock_product_repository.update_product = MagicMock()
    updated_product = product_service.update_product(1, "New Product", "New description", 15.0)
    mock_product_repository.update_product.assert_called_once_with(updated_product)
    assert updated_product.name == "New Product"
    assert updated_product.description == "New description"
    assert updated_product.price == 15.0

# Test for update_product method with non-existent product

def test_update_product_non_existent(product_service, mock_product_repository):
    mock_product_repository.get_product_by_id = MagicMock(return_value=None)
    with pytest.raises(ValueError, match="Product does not exist"):
        product_service.update_product(1, "New Product", "New description", 15.0)
