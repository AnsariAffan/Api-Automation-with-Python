import os
import sys
import shutil
from pathlib import Path
import pytest
from clients.product_client import ProductClient

# 1. Stop Python from creating bytecode (.pyc files)
sys.dont_write_bytecode = True

# 2. Shared Fixture: Creates the API client once for all tests
@pytest.fixture(scope="session")
def product_client():
    return ProductClient()

# 3. Cleanup: Automatically deletes all __pycache__ folders when finished
def pytest_sessionfinish(session):
    root = Path(session.config.rootdir)
    for folder in root.rglob("__pycache__"):
        shutil.rmtree(folder, ignore_errors=True)
