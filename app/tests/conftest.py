import os
import sys

import pytest

# Make `app.py` importable regardless of the working directory pytest is run
# from, by adding the app package directory (the parent of this tests dir) to
# the import path.
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
