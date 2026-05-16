# API Automation Framework with Python

A professional, Page Object Model (POM) based API automation framework designed for scalability and maintainability.

## 🚀 Features
- **Page Object Model (POM)**: Separation of API clients and test logic.
- **Full CRUD Coverage**: Complete Create, Read, Update, and Delete test cycles.
- **Dynamic Data**: Integration with **Faker** for realistic, randomized test data.
- **Auto-Cleanup**: Automatically removes `__pycache__` and `.pytest_cache` folders after every run to keep the project clean.
- **Custom Markers**: Categorized tests using `@pytest.mark.smoke` and `@pytest.mark.regression`.

## 🛠 Tech Stack
- **Python 3.x**
- **Pytest**: Testing framework.
- **Requests**: HTTP library for API interaction.
- **Faker**: For generating dynamic test data.

## 📁 Project Structure
```text
├── clients/              # API Page Objects (Inheritance-based)
│   ├── base_client.py    # Common logic (headers, session)
│   └── product_client.py # Product-specific endpoints
├── tests/                # Test suites
│   └── test_products.py  # Full CRUD and negative test cases
├── config/               # Environment configuration
│   └── config.py         # Base URLs and timeouts
├── conftest.py           # Shared fixtures and auto-cleanup hooks
├── pytest.ini            # Pytest configuration and marker registration
└── requirements.txt      # Project dependencies
```

## 🏁 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run All Tests
```bash
python -m pytest
```

### 3. Run Specific Categories
- **Smoke Tests**: `python -m pytest -m smoke`
- **Regression Tests**: `python -m pytest -m regression`

## 🔗 Dummy API Used
This project uses [FakeStoreAPI](https://fakestoreapi.com) for demonstration purposes.
