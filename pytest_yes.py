"""
A pytest plugin to print YES against each test.
"""

import pytest

__version__ = "0.0.1"

def pytest_configure(config):
    config.addinivalue_line("markers", "yes: mark test as slow to run")

def pytest_addoption(parser):
    parser.addoption("--yes", action="store_true", help="include tests marked slow")

def pytest_collection_modifyitems(config, items):
    if config.getoption('--yes'):
        for test_obj in items:
            print('->', test_obj, '-> YES')



