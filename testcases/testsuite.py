import unittest
from testcases.test001_login_test import LoginTests
from testcases.LayOut_Floor_Plan.test_layout_floor_plan import FloorPlanTest
from testcases.global_catalog.test_global_catalog001 import GlobalCatalogTest

# Get all tests from the test classes

tc3 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc1 = unittest.TestLoader().loadTestsFromTestCase(FloorPlanTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(GlobalCatalogTest)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc3, tc1, tc2])


unittest.TextTestRunner(verbosity=2).run(smokeTest)



