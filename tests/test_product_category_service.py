import pytest
from unittest.mock import MagicMock
from backend.services.product.product_category_service import ProductCategoryService
from backend.models.product.product_category import ProductCategory

# Fixtures for mock repository
@pytest.fixture
def mock_category_repository():
    return MagicMock()

@pytest.fixture
def product_category_service(mock_category_repository):
    return ProductCategoryService(mock_category_repository)

# Test for assign_category_to_product method

def test_assign_category_to_product(product_category_service, mock_category_repository):
    mock_category_repository.add_product_category = MagicMock()
    product_category = product_category_service.assign_category_to_product(1, 2)
    mock_category_repository.add_product_category.assert_called_once_with(ProductCategory(1, 2))
    assert product_category.product_id == 1
    assert product_category.category_id == 2

# Test for get_categories_for_product method

def test_get_categories_for_product(product_category_service, mock_category_repository):
    mock_category_repository.get_categories_by_product_id = MagicMock(return_value=[1, 2, 3])
    categories = product_category_service.get_categories_for_product(1)
    mock_category_repository.get_categories_by_product_id.assert_called_once_with(1)
    assert categories == [1, 2, 3]

# Test for get_products_for_category method

def test_get_products_for_category(product_category_service, mock_category_repository):
    mock_category_repository.get_products_by_category_id = MagicMock(return_value=[4, 5, 6])
    products = product_category_service.get_products_for_category(2)
    mock_category_repository.get_products_by_category_id.assert_called_once_with(2)
    assert products == [4, 5, 6]