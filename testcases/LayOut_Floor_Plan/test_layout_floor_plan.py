import unittest
import pytest

from utilities.util import *
from pages.Floor.test_floor_pages import Floor_Plan


@pytest.mark.run(order=2)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.floor = Floor_Plan(self.driver)

    def test_001_Verify_Floor_Plan_Navigation(self):
        self.floor = Floor_Plan(self.driver)
        self.floor.Floor_plan_Navigation()
