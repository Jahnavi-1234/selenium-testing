import pytest
from base.base_class import BaseClass

@pytest.fixture(scope="function")
def driver():
    base = BaseClass()
    driver = base.init_driver()
    yield driver
    driver.quit()
