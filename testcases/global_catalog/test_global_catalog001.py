import unittest
import pytest

from utilities.util import *
from pages.global_catalog.test001_global_catalog_page import GlobalCatalog1


@pytest.mark.run(order=1)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.gcatalog = GlobalCatalog1(self.driver)

    def test_001_Verify_Filters_Label(self):
        """Verify all filter's label."""
        self.gcatalog.filterLabel()
        self.gcatalog.collectionFilter()
        self.gcatalog.WarehouseFiler()
        self.gcatalog.CountryFilter()
        self.gcatalog.typeFilter()
        self.gcatalog.subTypeFilter()
        self.gcatalog.colorfamilyFilter()
        self.gcatalog.manufactureFilter()
        self.gcatalog.materialFilter()
        self.gcatalog.lightingtagFilter()
        self.gcatalog.lowvoltageFilter()

    def test_002_Verify_See_Morelinks(self):
        self.gc = GlobalCatalog1(self.driver)
        self.gc.checkSeeMorelink()

    def test_003_Verify_apply_Filter(self):
        """Verify reset filter """
        self.gc = GlobalCatalog1(self.driver)
        self.gc.applyFilter()

    def test_04_Verify_Applied_Filter_Results(self):
        """Verify product detail page """
        self.gc = GlobalCatalog1(self.driver)
        self.gc.verifyAppliedFilterDetailPage()

    def test_05_Verify_Qty_In_Warehouse(self):
        """Verify Quantity in warehouse"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.QtyWarehouse()

    def test_06_Verify_Country_availability(self):
        """Verify country availability"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.Country_availability()

    def test_07_Verify_Lighting_Tag(self):
        """Verify Lighting tag feature in Project Detailed page"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.Lighting_Tag()

    def test_08_Verify_Bulk2_Tag(self):
        """Verify Collection - Bulk tag """
        self.gc = GlobalCatalog1(self.driver)
        self.gc.filterTagBulk2()

    def test_09_Verify_Custom_Tag(self):
        """Verify Collection - Custom tag"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.filterTagCustom()

    def test_10_Verify_NorthAmerica2020_Tag(self):
        """Verify all Collection - North-america 2020 tag"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.filterTagNorthAmerica2020()

    def test_11_Verify_Phoenix_Tag(self):
        """Verify Collection Phoenix tag"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.filterTagPhoenix()

    def test_12_Verify_Sort_By_Lowest_Price(self):
        """Verify Product Sorting by lowest price"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.clickSortLowestDropdown()

    def test_13_Verify_Sort_By__Highest_price(self):
        """Verify Product Sorting by highest price"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.sorthighest1()

    def test_14Verify_Sort_By__Highest_Rating(self):
        """Verify Product Sorting by Highest Rating"""
        self.gc = GlobalCatalog1(self.driver)
        self.gc.sortRating()

    #def test_15_Verify_Sort_By__Most_Reviewed(self):
    #    self.gc = GlobalCatalog1(self.driver)
    #    self.gc.sortmostreviewed()

    def test_16_Verify_by_Textbox_Searchg(self):
        self.gc = GlobalCatalog1(self.driver)
        self.gc.searchBox()

    def test_17_Verify_Exact_SKU(self):
        self.gc = GlobalCatalog1(self.driver)
        self.gc.skuSearch()

    def test_18_Verify_SKU_After_Character_Trim(self):
        self.gc = GlobalCatalog1(self.driver)
        self.gc.skuSearchCharTrim()

    def test_19_Verify_SKU_If_Character_Lower(self):
        self.gc = GlobalCatalog1(self.driver)
        self.gc.skuSearch_LowerChar()

    def test_20_Verify_SKU_After_Fist_and_Last_Character_Trim(self):
        self.gc = GlobalCatalog1(self.driver)
        self.gc.skuSearch_FirstLastChTrim()
