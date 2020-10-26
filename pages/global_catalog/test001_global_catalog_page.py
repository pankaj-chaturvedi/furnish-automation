import time
from selenium.webdriver.common.keys import Keys

from base.selenium_driver import SeleniumDriver

class GlobalCatalog1(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


   # Locators :
    Catlog = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[2]/div/div/div[3]/div/a/div/div"
    filter = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[1]/h2"
    collection = "//h4[contains(text(),'Collection')]"
    warehouse =  "//h4[contains(text(),'Warehouse')]"
    Country = "//h4[contains(text(),'Country')]"
    type = "// h4[contains(text(), 'Type')]"
    Subtype= "// h4[contains(text(), 'Sub type')]"
    Colorfamily = "//h4[contains(text(),'Color family')]"
    manufacturer = "//h4[contains(text(),'Manufacturer')]"
    vendor = "//h4[contains(text(),'Vendor')]"
    materialtype = "//h4[contains(text(),'Material type')]"
    lightingtag = "//h4[contains(text(),'Lighting tag')]"
    lowvoltage = "//h4[contains(text(),'Low voltage')]"
    project = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[2]/div/div/div[1]/div/a/div/div"

    def filterLabel(self):
        actual = 'Filters'
        self.element_click(self.Catlog)
        filter_label = self.get_text(self.filter)
        self.verify_text_contains(actual_text=filter_label, expected_text=actual)

    def collectionFilter(self):
        actual = 'Collection'
        self.element_click(self.Catlog)
        label = self.get_text(self.collection)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def WarehouseFiler(self):
        actual = 'Warehouse'
        self.element_click(self.Catlog)
        label = self.get_text(self.warehouse)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def CountryFilter(self):
        actual = 'Country'
        self.element_click(self.Catlog)
        label = self.get_text(self.Country)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def typeFilter(self):
        actual = 'Type'
        self.element_click(self.Catlog)
        label = self.get_text(self.type)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def subTypeFilter(self):
        actual = 'Sub type'
        self.element_click(self.Catlog)
        label = self.get_text(self.Subtype)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def manufactureFilter(self):
        actual = 'Manufacturer'
        self.element_click(self.Catlog)
        label = self.get_text(self.manufacturer)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def vendorFilter(self):
        actual = 'Vendor'
        self.element_click(self.Catlog)
        label = self.get_text(self.vendor)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def materialFilter(self):
        actual = 'Material type'
        self.element_click(self.Catlog)
        label = self.get_text(self.materialtype)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def colorfamilyFilter(self):
        actual = 'Color family'
        self.element_click(self.Catlog)
        label = self.get_text(self.Colorfamily)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    def lightingtagFilter(self):
         actual = 'Lighting tag'
         self.element_click(self.Catlog)
         label = self.get_text(self.lightingtag)
         self.verify_text_contains(actual_text=label, expected_text=actual)

    def lowvoltageFilter(self):
        actual = 'Low voltage'
        self.element_click(self.Catlog)
        label = self.get_text(self.lowvoltage)
        self.verify_text_contains(actual_text=label, expected_text=actual)

    Collection_position = "//h4[contains(text(),'Collection')]"
    see_more = "//div[1]//span[contains(text(),'See more')]"
    #old = "//div[4]//ul[1]//li[7]//span[1]"
    see_less = "//span[contains(text(),'See Less')]"

    def checkSeeMorelink(self):
        time.sleep(4)
        self.element_click(self.Catlog)
 #      if self.is_element_present(self.Country_position) == True:
        self.element_click(self.see_more)
        time.sleep(2)
        see_less = self.get_text(self.see_less)
        text = "See Less"
        self.verify_text_contains(actual_text=see_less, expected_text=text)
        time.sleep(2)
        self.element_click(self.see_less)
        time.sleep(2)
        see_more = self.get_text(self.see_more)
        text = "See more"
        self.verify_text_contains(actual_text=see_more, expected_text=text)

    _filter_click = "//label[contains(.,'Bulk 1.0')]"
    _clear_filter = "//p[contains(text(),'Reset filters')]"

    def applyFilter(self):
        time.sleep(2)
        self.element_click(self.Catlog)
        self.web_scroll(direction="up")
        self.wait_for_element(self._filter_click)
        self.element_click(self._filter_click)
        time.sleep(2)
        self.wait_for_element(self._clear_filter)
        clear_filter = self.get_text(self._clear_filter)
        self.verify_text_contains(actual_text=clear_filter, expected_text='Reset filters')
        time.sleep(2)

 # Check filter values after applying the filters.

    # Applied filter on listing screen
    _type_select = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[5]/ul/li[1]/label/div[2]/div/span[1]"
    _sub_type_click = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[6]/ul/li[1]/label/div[2]/div/span[1]"
    _manufacture_click = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[8]/ul/li[1]/label/div[2]/div/span[1]"

    # detail page filter value verification
    _manufacture_value = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[6]/div[2]/div/div/div/div[2]/span[2]"
    _type_value = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[6]/div[2]/div/div/div/div[7]/span[2]"
    _subtype_value = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[6]/div[2]/div/div/div/div[8]/span[2]"

    # click on first cell after applying the filter

    _first_cell = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a[1]"

    def verifyAppliedFilterDetailPage(self):
        """ verify result after click on manufacturer , type and subtype"""
        time.sleep(2)
        self.element_click(self.Catlog)
        collection = self.get_text(self._filter_click)
        self.element_click(self._type_select)
        time.sleep(2)
        typefilter = self.get_text(self._type_select)
        time.sleep(3)
        self.element_click(self._sub_type_click)
        sub_type = self.get_text(self._sub_type_click)
        time.sleep(3)
        self.element_click(self._manufacture_click)
        manufacture = self.get_text(self._manufacture_click)
        time.sleep(3)
        self.element_click(self._first_cell)
        time.sleep(3)
        subtype_detail_value = self.get_text(self._subtype_value)
        type_detail_value = self.get_text(self._type_value)
        manufacture_detail_value = self.get_text(self._manufacture_value)
        self.verify_text_contains(actual_text=typefilter, expected_text=type_detail_value)
        self.verify_text_contains(actual_text=sub_type, expected_text=subtype_detail_value)
        self.verify_text_contains(actual_text=manufacture, expected_text=manufacture_detail_value)
        print("typefilter->",type_detail_value, "|| sub_type filter->",subtype_detail_value,"||manufacture",manufacture_detail_value)
        self.element_click(self.project)
        time.sleep(2)

    # Locator for search product form global catalog
    _search_box = "//input[@placeholder='Filter by product name, SKU']"
    _product_name = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a[1]/div[2]/span[1]"

    """search product via search box"""
    def searchBox(self):
        time.sleep(5)
        self.element_click(self.Catlog)
        time.sleep(3)
        product_name = self.get_text(self._product_name)
        time.sleep(2)
        self.element_click(self._search_box)
        time.sleep(4)
        self.EnterProductName(str(product_name))
        time.sleep(2)
        self.pressEnter(Keys.RETURN)
        time.sleep(2)
        SearchedResult = self.get_text(self._product_name)
        self.verify_text_contains(actual_text=product_name, expected_text=SearchedResult)
        print("actual_text=", product_name, "expected_text=",SearchedResult)
        self.element_click(self.project)
        time.sleep(5)


        '''second_product = self.getText(self._second_product_name)
        time.sleep(2)
        second_product = second_product.split()
        for i in second_product:
            if i == 'Rustic':
                return True
            elif i == 'copper':
                return True
            elif i == 'wallet':
                return True
            else:
                return False'''

    def EnterProductName(self, value):
        time.sleep(2)
        self.clear_field(self._search_box)
        time.sleep(2)
        self.send_keys(value, self._search_box)

    def pressEnter(self, value):
        self.send_keys(value, self._search_box)



    _sku = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a[1]/div[2]/span[2]"
    _custom_sku = "//p[contains(text(),'+ Custom SKU')]"

    def skuSearch(self):
        """Verify SKU once with exact match is match"""
        time.sleep(2)
        self.element_click(self.Catlog)
        sku_text = self.get_text(self._sku)
        time.sleep(1)
        self.element_click(self._search_box)
        time.sleep(4)
        self.EnterProductName(str(sku_text))
        time.sleep(2)
        self.pressEnter(Keys.RETURN)
        time.sleep(2)
        sku_result = self.get_text(self._sku)
        time.sleep(2)
        self.verify_text_contains(actual_text=sku_text, expected_text=sku_result)
        print("actual_text=", sku_text, "expected_text=",sku_result)
        self.clear_field(self._search_box)
        time.sleep(2)
        self.element_click(self.project)
        time.sleep(5)

    def skuSearchCharTrim(self):
        """Verify SKU once first character is trim"""
        time.sleep(5)
        self.element_click(self.Catlog)
        sku_text = self.get_text(self._sku)
        sku_textFC = sku_text[1:]
        self.EnterProductName(sku_textFC)
        time.sleep(5)
        self.pressEnter(Keys.ENTER)
        time.sleep(5)
        sku_result1 = self.get_text(self._sku)
        self.verify_text_contains(actual_text=sku_result1, expected_text=sku_text)
        print("First character trim - ", sku_textFC, "Actual result-", sku_result1, "Expected text-",sku_text)
        self.clear_field(self._search_box)
        self.element_click(self.project)
        time.sleep(5)

    def skuSearch_LowerChar(self):
        """Verify SKU with lower text"""
        time.sleep(5)
        self.element_click(self.Catlog)
        sku_result2 = self.get_text(self._sku)
        sku_textlower = sku_result2.lower()
        self.EnterProductName(sku_textlower)
        time.sleep(5)
        self.pressEnter(Keys.ENTER)
        time.sleep(5)
        sku_result1 = self.get_text(self._sku)
        self.verify_text_contains(actual_text=sku_textlower, expected_text=sku_result1)
        print("actual_text=",sku_textlower, "expected_text=",sku_result1)
        self.clear_field(self._search_box)
        self.element_click(self.project)
        time.sleep(5)

    def skuSearch_FirstLastChTrim(self):
        """Verify SKU with frist and last character trim"""
        time.sleep(5)
        self.element_click(self.Catlog)
        removed_Actual_sku = self.get_text(self._sku)
        removed_FirstCharcterTrim_sku = removed_Actual_sku[1:]
        removed_LastCharcterTrim_sku = removed_FirstCharcterTrim_sku[:-1]
        time.sleep(5)
        self.EnterProductName(removed_LastCharcterTrim_sku)
        time.sleep(5)
        self.pressEnter(Keys.ENTER)
        time.sleep(5)
        sku_result3 = self.get_text(self._sku)
        self.verify_text_contains(actual_text=sku_result3, expected_text=removed_Actual_sku)
        print("Actual result -", sku_result3 , "Expected result-", removed_Actual_sku)
        self.clear_field(self._search_box)
        time.sleep(2)
        self.element_click(self.project)
        time.sleep(5)

    _click_most_relevant_dropdown = "//div[@id='root']//div[contains(text(),'Most relevant')]"
    _click_sort_by_lowest = "//div[@id='root']//div[contains(text(),'Sort by lowest price')]"
    _click_sort_by_highest = "//div[@id='root']//div[contains(text(),'Sort by highest price')]"
    _click_sort_by_rating = "//div[@id='root']//div[contains(text(),'Sort by highest rating')]"
    _click_sort_by_most_reviewed = "//div[@id='root']//div[contains(text(),'Sort by most reviewed')]"


    def pressDownKey(self, value):
        self.send_keys(value, self._click_most_relevant_dropdown)

    def pressEnterSortSelection(self, value):
        self.send_keys(value, self._click_most_relevant_dropdown)

    def clickSortLowestDropdown(self):

        time.sleep(4)
        self.element_click(self.Catlog)
        time.sleep(2)
        self.element_click(self._click_most_relevant_dropdown)
        time.sleep(5)
        a = self.element_click(self._click_sort_by_lowest)
        self.log.info(a)
        time.sleep(4)
        self.log.info("hi this is a print")
        a = "//body/div[@id='root']//div"
        c = '/div[1]/div[2]/div[1]//span[1]'
        list = []
        for i in range(2, 25):
            x = [i]
            price_xpath = a + str(x) + c
            time.sleep(4)
            if self.is_element_present(price_xpath) == False:
                break
            else:
                price = self.get_text(price_xpath)
                price = price.replace("$", '')
                price = price.replace(",", '')
                (list.append(float(price)))
        self.log.info("Original list : " + str(list))
        # using all() to
        # check sorted list
        flag = 0
        if (list == sorted(list)):
            flag = 1
        # printing result
        if (flag):
            self.log.info("Yes, List is sorted.")
            return True
        else:
            self.log.info("No, List is not sorted.")
            return False

    GC_link = "//*[@id='main-container']/main/div/div/div[1]/span[1]"
    Rating = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/p[1]"
    def sortRating(self):
        """test_14Verify_Sort_By__Highest_Rating"""
        time.sleep(4)
        self.element_click(self.Catlog)
        time.sleep(2)
        self.element_click(self._click_most_relevant_dropdown)
        time.sleep(5)
        self.element_click(self._click_sort_by_rating)
        time.sleep(5)
        card1 = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a["
        card2 = "]/div[1]"
        list = []
        for i in range(2, 25):
            _path = card1 + str(i) + card2
            self.element_click(_path)
            time.sleep(5)
            RatingValue = self.get_text(self.Rating)
            #RatingValue = RatingValue.replace("0", '')
            #RatingValue = RatingValue.replace(".", '')
            list.append(float(RatingValue))
            self.element_click(self.GC_link)
        ExpResult = "True"
        if(list == sorted(list,reverse=True)):
            ActResult = "True"
            print("list is sorted",list)
        else:
            ActResult = "False"
            print("list is not sorted",list)
        self.verify_text_match(ActResult,ExpResult)


    # Qtywarehouse locators for xpath
    QtyWarehouse = "//h4[contains(text(),'Qty in warehouse')]"
    QtywarehouseValue = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[3]/ul/ul/div/div[1]/div/div/input"
    warehouseCheckbox_xpath = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[3]/ul/li[1]/label/div[2]/div/span[1]"
    Applybutton_qty ="//*[@id='main-container']/main/div/div/div/div[1]/div/div[3]/ul/ul/div/button/span"
    QtyResult_card = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a[1]"
    Availibility = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[4]/div[1]/span[1]"
    warehousenameExpted = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[4]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div/div/div/strong"
    QtyActualvaluepath = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[4]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div/div"

    def QtyWarehouse(self):
      time.sleep(2)
      self.element_click(self.Catlog)
      time.sleep(2)
      expvalueWarehouse=self.get_text(self.warehouseCheckbox_xpath)
      self.element_click(self.warehouseCheckbox_xpath)
      time.sleep(2)
      self.element_click(self.QtywarehouseValue)
      time.sleep(2)
      self.clear_field(self.QtywarehouseValue)
      time.sleep(2)
      self.send_keys(50, self.QtywarehouseValue)
      time.sleep(2)
      self.element_click(self.Applybutton_qty)
      time.sleep(2)
      self.element_click(self.QtyResult_card)
      time.sleep(2)
      self.element_click(self.Availibility)
      time.sleep(2)
      QtyinwarehouseActualvalue=self.get_text(self.QtyActualvaluepath)
      warehouseActualValue = self.get_text(self.warehousenameExpted)
      if(int(QtyinwarehouseActualvalue)<50):
         print("condition does not match")
      else:
        self.verify_text_contains(actual_text=warehouseActualValue, expected_text=expvalueWarehouse)
        print("actual_text=", warehouseActualValue, "expected_text=",expvalueWarehouse)
      self.element_click(self.project)
      time.sleep(5)

    #loctaor for country availability
    Countrychebox = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[4]/ul/li[1]/label"
    Country_Availabitly_actual = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[4]/div[2]/div/div/div/div[3]/strong"
    #Country_avl_label = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[4]/div[2]/div/div/div/strong[2]"

    def Country_availability(self):
        """Verify Quantity in warehouse"""
        time.sleep(2)
        self.element_click(self.Catlog)
        time.sleep(4)
        self.element_click(self.Countrychebox)
        CA_Expected = self.get_text(self.Countrychebox)
        CA_Expected = CA_Expected[:-5]
        time.sleep(4)
        self.element_click(self.QtyResult_card)
        time.sleep(5)
        self.element_click(self.Availibility)
        time.sleep(5)
        #CAL=self.get_text(self.Country_avl_label)
        CA_Actual=self.get_text(self.Country_Availabitly_actual)
        CA_Actual= CA_Actual.strip()
        #if self.is_element_present(CAL) == False:
        #print("Country does not exit")
        #else:
        self.verify_text_contains(actual_text=CA_Actual.strip(),expected_text=CA_Expected.strip())
        print("Country availabilty excepted value ->",CA_Expected, "||Country availabilty excepted value ->", CA_Actual)
        self.element_click(self.project)
        time.sleep(5)

    #locator for lighting tag
    ligtingCheckbox = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[11]/ul/li[1]/label"
    product_card_result = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a[1]"
    Ligting_information_pdp = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[6]/div[2]/div/div/div[2]/div/div[1]/span[1]"
    lighting_fixer = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[6]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/span[2]"

    def Lighting_Tag(self):
        """Verify Lighting Tags in PDP"""
        time.sleep(5)
        self.element_click(self.Catlog)
        time.sleep(4)
        self.element_click(self.ligtingCheckbox)
        time.sleep(4)
        ExpValue_Lighting_Tag = self.get_text(self.ligtingCheckbox)
        ExpValue_Lighting_Tag = ExpValue_Lighting_Tag[:4]
        self.element_click(self.product_card_result)
        time.sleep(5)
        LightingTag_label = self.get_text(self.Ligting_information_pdp)
        Actual_value_lightingTag = self.get_text(self.lighting_fixer)
        if LightingTag_label in ("Lighting information"):
           self.verify_text_contains(actual_text=Actual_value_lightingTag.strip(),expected_text=ExpValue_Lighting_Tag.strip())
           print("actvalue =", Actual_value_lightingTag, "ExpValue =", ExpValue_Lighting_Tag)
        else:
           print("Lighting information label does not found")
           print(LightingTag_label)
        self.element_click(self.project)
        time.sleep(5)

 # Verify tag selected from left side should show expected list accordingly.

    _bulk_tag = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a[1]/div[2]/div/div/div[1]"
    collection_see_more = "//div[@id='root']/div/div[3]/div/div/div[2]/div/div/div[3]/ul/li[7]/span"

    _bulk_2 = "//label[contains(.,'Bulk 2.0')]"
    def filterTagBulk2(self):
        time.sleep(5)
        self.element_click(self.Catlog)
        time.sleep(4)
        self.element_click(self._bulk_2)
        name = self.get_text(self._bulk_2)
        name = name[:-4]
        time.sleep(2)
        bulk_tag_text = self.get_text(self._bulk_tag)
        time.sleep(2)
        self.verify_text_contains(actual_text=bulk_tag_text.strip(), expected_text=name.strip())
        print("actual_text",bulk_tag_text, "expected_text",name)
        self.element_click(self.project)
        time.sleep(5)
        self.element_click(self.project)
        time.sleep(5)


    _custom_tag = "//label[contains(.,'Custom')]"

    def filterTagCustom(self):
        time.sleep(5)
        self.element_click(self.Catlog)
        time.sleep(4)
        self.element_click(self._custom_tag)
        name = self.get_text(self._custom_tag)
        name = name[:-5]
        time.sleep(2)
        bulk_tag_text = self.get_text(self._bulk_tag)
        bulk_tag_text1 = bulk_tag_text.lower()
        time.sleep(2)
        self.verify_text_contains(actual_text=bulk_tag_text1.strip(),expected_text=name.strip())
        print("actual_text",bulk_tag_text, "expected_text=",name)
        self.element_click(self.project)
        time.sleep(5)

    _NorthAmerica2020_tag = "//label[contains(.,'NorthAmerica2020')]"
    _pdp_tag = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div"

    def filterTagNorthAmerica2020(self):
        time.sleep(5)
        self.element_click(self.Catlog)
        time.sleep(4)
        self.element_click(self.see_more)
        time.sleep(2)
        self.element_click(self._NorthAmerica2020_tag)
        name = self.get_text(self._NorthAmerica2020_tag)
        name = name[:-5]
        time.sleep(2)
        self.element_click(self._first_cell)
        _pdp_tag_text = self.get_text(self._pdp_tag)
        PD_Tag1 = _pdp_tag_text.lower()
        time.sleep(2)
        self.verify_text_contains(actual_text=PD_Tag1.strip(), expected_text=name.strip())
        print("actual_text", PD_Tag1, "expected_text=", name)
        self.element_click(self.project)
        time.sleep(5)

    _phoenix_tag = "//label[contains(.,'Phoenix')]"

    def filterTagPhoenix(self):
        time.sleep(5)
        self.element_click(self.Catlog)
        time.sleep(4)
        self.element_click(self.see_more)
        time.sleep(2)
        self.element_click(self._phoenix_tag)
        name = self.get_text(self._phoenix_tag)
        name = name[:-5]
        time.sleep(2)
        bulk_tag1= self.get_text(self._bulk_tag)
        bulk_tag2 = bulk_tag1.lower()
        time.sleep(2)
        self.verify_text_contains(actual_text=bulk_tag2.strip(), expected_text=name.strip())
        print("Actual_text=",bulk_tag2 ,"expected_text=",name)
        self.element_click(self.project)
        time.sleep(5)

    PD = "//*[@id='main-container']/main/div/div/div[1]/span[1]"
    def sortmostreviewed(self):
        """test_15_Verify_Sort_By__Most_Reviewed"""
        time.sleep(4)
        self.element_click(self.Catlog)
        time.sleep(2)
        self.element_click(self._click_most_relevant_dropdown)
        time.sleep(5)
        self.element_click(self._click_sort_by_most_reviewed)
        time.sleep(5)
        time.sleep(5)
        card1 = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a["
        card2 = "]/div[1]"
        list = []
        for i in range(2, 25):
            _path = card1 + str(i) + card2
            self.element_click(_path)
            time.sleep(5)
            review = "//*[@id='main-container']/main/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/p[2]"
            ReviewsValue = self.get_text(review)
            ReviewsValue = ReviewsValue.replace("See", '')
            ReviewsValue = ReviewsValue.replace("reviews", '')
            ReviewsValue = ReviewsValue.replace("one review", '')
            #print(ReviewsValue)
            self.element_click(self.PD)
            list.append(float(ReviewsValue))
        self.log.info(list)
        flag = 0
        if (list == sorted(list, reverse=True)):
           self.log.info("Yes, List is sorted.")
        else:
            self.log.info("No, List is not sorted.")
        self.element_click(self.project)


    #PD = "//*[@id='main-container']/main/div/div/div[1]/span[1]"
    def sorthighest1(self):
        """test_13_Verify_Sort_By__Highest_price"""
        time.sleep(4)
        self.element_click(self.Catlog)
        time.sleep(2)
        self.element_click(self._click_most_relevant_dropdown)
        time.sleep(5)
        a = self.element_click(self._click_sort_by_highest)
        time.sleep(3)
        card1 = "//*[@id='main-container']/main/div/div/div/div[2]/div/div[2]/a["
        card2 = "]/div[2]/div/span"
        list = []
        for i in range(2, 25):
            _path = card1 + str(i) + card2
            pricevalue = self.get_text(_path)
            time.sleep(5)
            pricevalue = pricevalue.replace("$", '')
            pricevalue = pricevalue.replace(",", '')
            list.append(float(pricevalue))
        ExpResult = "True"
        if (list == sorted(list, reverse=False)):
                flag = "True"
                print("Yes, List is sorted.")
        else:
                flag = "False"
                print("No, List is not sorted.")
        self.verify_text_contains(ExpResult,flag)
        self.element_click(self.project)


