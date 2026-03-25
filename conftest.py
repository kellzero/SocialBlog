import os
import sys
from pathlib import Path

import django


def pytest_configure():
    # Add project root to Python path
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))

    # Set Django settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")

    # Setup Django
    django.setup()
