import pytest
from backend.models.product.product import Product

# Test for Product creation with valid data

def test_create_product_with_valid_data():
    product = Product(1, "Test Product", "This is a test product", 10.0)
    assert product.product_id == 1
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 10.0

# Test for Product creation with zero price

def test_create_product_with_zero_price():
    with pytest.raises(ValueError, match="Price must be a positive number"):
        Product(1, "Test Product", "This is a test product", 0)

# Test for Product creation with negative price

def test_create_product_with_negative_price():
    with pytest.raises(ValueError, match="Price must be a positive number"):
        Product(1, "Test Product", "This is a test product", -5.0)

# Test for Product creation with empty name

def test_create_product_with_empty_name():
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product(1, "", "This is a test product", 10.0)

# Test for Product creation with empty description

def test_create_product_with_empty_description():
    with pytest.raises(ValueError, match="Product description cannot be empty"):
        Product(1, "Test Product", "", 10.0)
