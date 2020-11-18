import unittest
import pytest

from utilities.util import *
from pages.Floor.test_floor_pages import Floor_Plan


@pytest.mark.run(order=1)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.floor = Floor_Plan(self.driver)

    def test_001_Verify_Floor_Plan_Navigation(self):
        self.floor = Floor_Plan(self.driver)
        self.floor.Floor_plan_Navigation()

    def test_002_Verify_Floor_plan_Errors(self):
        self.floor = Floor_Plan(self.driver)
        self.floor.Floor_plan_Error_SVG_NOT_FOUND()

    def test_003_verify_sync_floor_plan_via_lastsync_refresh_button(self):
        self.floor = Floor_Plan(self.driver)
        self.floor.sync_floor_plan_Lastsync_button()

    def test_004_verify_floor_plan(self):
            self.floor = Floor_Plan(self.driver)
            self.floor.verify_floorPlan()

    #def test_005_verify_Sync_with_Harvester_button(self):
    #    self.floor = Floor_Plan(self.driver)
    #    self.floor.Sync_with_Harvester()



