import time
from builtins import print
from select import select

from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
# import Alert
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class Floor_Plan(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    Your_project = "//*[@id='main-container']/main/div/div/div/div[2]/div[1]/div[2]/div"
    #Back = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[1]/div"
    Floor_Plan = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/a/div/div"
    Back_floor = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[1]/div/a/strong"

    def currenturl(self):
        get_url = driver.current_url
        print(get_url)

    def Floor_plan_Navigation(self):
        time.sleep(2)
        self.element_click(self.Your_project)
        time.sleep(2)
        self.element_click(self.Floor_Plan)
        time.sleep(2)
        get_url = self.driver.current_url
        substring = "floorplan"
        ExpectedResult = "True"
        if substring in get_url:
            print("Floor page navigates successfully",get_url )
            Actual_flag = "True"
        else:
            print("not get get_url",get_url)
            Actual_flag = "False"
        self.verify_text_contains(ExpectedResult,Actual_flag)
        self.element_click(self.Back_floor)


    image = "//*[@aug-id='72b9b12c-18ed-11eb-9f06-9507b1507856']"
    alert = "//div[@class='Toastify__toast-body']"


    def Floor_plan_Error_SVG_NOT_FOUND(self):
        time.sleep(5)
        self.element_click(self.Your_project)
        time.sleep(3)
        self.element_click(self.Floor_Plan)
        time.sleep(2)
        Actual_AlertMessage = self.get_text(self.alert)
        time.sleep(2)
        SVG_ERROR_ALERT = "Please re-harvest the Revit model and try again. (Error code: SVG_NOT_FOUND)"
        UNKNOWN_ERROR_ALERT = "Oh, there is a problem with the SRS (Spatial Resource Service). Please try again later. (Error code: UNKNOWN_ERROR_FROM_SRS)"
        Bound_Nan = "Please re-harvest the Revit model and try again. (Error code: BOUNDS_NAN)"
        Error_retrieving_project = "Oh no! There were some issues retrieving this project."
        Heads_up_error = "Heads up! There were some issues retrieving the project's spaces."
        Casefail = "It is bug"
        if SVG_ERROR_ALERT in Actual_AlertMessage:
            self.verify_text_contains(Actual_AlertMessage,SVG_ERROR_ALERT)
            print("Actual_AlertMessage->",Actual_AlertMessage,"Expected_Alert_Message-->", SVG_ERROR_ALERT)
        elif UNKNOWN_ERROR_ALERT in Actual_AlertMessage:
            self.verify_text_contains(Actual_AlertMessage, UNKNOWN_ERROR_ALERT)
            print("Actual_AlertMessage->", Actual_AlertMessage, "Expected_Alert_Message-->", UNKNOWN_ERROR_ALERT)
        elif Bound_Nan in Actual_AlertMessage:
            self.verify_text_contains(Actual_AlertMessage, Bound_Nan)
            print("Actual_AlertMessage->", Actual_AlertMessage, "Expected_Alert_Message-->", Bound_Nan)
        elif error_retrieving_project in Actual_AlertMessage:
            self.verify_text_contains(Actual_AlertMessage, Bound_Nan)
            print("Actual_AlertMessage->", Actual_AlertMessage, "Expected_Alert_Message-->", error_retrieving_project)
        elif Error_retrieving_project in Actual_AlertMessage:
            self.verify_text_contains(Actual_AlertMessage, Error_retrieving_project)
            print("Actual_AlertMessage->", Actual_AlertMessage, "Expected_Alert_Message-->", Error_retrieving_project)
        elif Heads_up_error in Actual_AlertMessage:
            self.verify_text_contains(Actual_AlertMessage, Heads_up_error)
            print("Actual_AlertMessage->", Actual_AlertMessage, "Expected_Alert_Message-->", Heads_up_error)
        else:
            self.verify_text_contains(Actual_AlertMessage, Casefail)
            print(Casefail)
        self.element_click(self.Back_floor)
        time.sleep(2)


    projetserach = "//input[@type='text']"
    alert1 = "//div[@role='alert']"
    imagep = "//*[@id='floorplan']/g/g/g[2]/g/g"
    button = "//*[@id='main-container']/main/div/div/div/div/div[1]/div/div[2]/button[1]"
    image1 = "#floorplan > g > g > g.content"
    def verify_floorPlan(self):
        time.sleep(2)
        self.element_click(self.projetserach)
        time.sleep(3)
        value = "525 Broadway - P1"
        self.send_keys(value, self.projetserach)
        time.sleep(5)
        self.element_click(self.Your_project)
        time.sleep(3)
        self.element_click(self.Floor_Plan)
        time.sleep(10)
        Actual_value = self.is_element_displayed(self.image1,locatorType='css')
        Expected_Value = "True"
        self.verify_text_contains(Expected_Value,str(Actual_value))
        self.element_click(self.Back_floor)

    lastSync_refresh_button = "//*[@id='main-container']/main/div/div/div/div[2]/div[2]/div/div[2]"
    sync_floor_plan_button = "//*[@id='root']/div[4]/div/div/div[3]/div/div/button[2]"
    success_message = "//*[@id='main-container']/main/div/div/div[1]/div/div[1]/span"
    def sync_floor_plan_Lastsync_button(self):
        self.element_click(self.Your_project)
        time.sleep(3)
        self.element_click(self.Floor_Plan)
        time.sleep(5)
        self.element_click(self.lastSync_refresh_button)
        time.sleep(5)
        self.element_click(self.sync_floor_plan_button)
        time.sleep(4)
        Exp_value = "Your floorplan is almost ready! We are busily working behind the scenes to display it. Check back in a few minutes."
        Actual_value = self.get_text(self.success_message)
        time.sleep(4)
        print("AR-->", Actual_value, "ER-->", Exp_value)
        self.verify_text_contains(Exp_value, Actual_value)
        self.element_click(self.Back_floor)

    sync_Harvester_button = "//*[@id='main-container']/main/div/div/div/div[1]/div/div[2]/button"
    SVG_ERROR_ALERT = "Please re-harvest the Revit model and try again. (Error code: SVG_NOT_FOUND)"
    harvested_not_compitible = "//*[@id='main-container']/main/div/div/div/div[1]/div/span"
    Floor_plan_unavailable = "//*[@id='main-container']/main/div/div/div[1]/div/span"
    workingOnIt_message = "//*[@id='main-container']/main/div/div/div[1]/div/div[1]/span/text()"
    def Sync_with_Harvester(self):
        time.sleep(5)
        self.element_click(self.Your_project)
        time.sleep(3)
        self.element_click(self.Floor_Plan)
        time.sleep(2)
        Actual_AlertMessage = self.get_text(self.alert)
        Act_message = self.get_text(self.harvested_not_compitible)
        harvest_msg_texton_page = "Harvested floor not compatible"
        floor_plan_unavailable_mgs_on_page_text = "Floor plan unavailable"
        _Act_floor_plan_unavailable_mgs_on_page = self.get_text(self.Floor_plan_unavailable)
        if self.SVG_ERROR_ALERT in Actual_AlertMessage:
            if harvest_msg_texton_page in Act_message:
                self.element_click(self.sync_Harvester_button)
                time.sleep(6)
                self.element_click(self.sync_floor_plan_button)
                time.sleep(5)
                Exp_value = "Your floor plan sync has been successfully requested. Please come back in 15-20 minutes to see the latest plans."
                Actual_value = self.get_text(self.success_message)
                time.sleep(4)
                print("AR-->", Actual_value, "ER-->", Exp_value)
                self.verify_text_contains(Exp_value, Actual_value)
                self.element_click(self.Back_floor)
            elif floor_plan_unavailable_mgs_on_page_text in _Act_floor_plan_unavailable_mgs_on_page:
                self.element_click(self.sync_Harvester_button)
                time.sleep(4)
                self.element_click(self.sync_floor_plan_button)
                time.sleep(4)
                self.verify_text_contains(floor_plan_unavailable_mgs_on_page_text,_Act_floor_plan_unavailable_mgs_on_page)
                self.element_click(self.Back_floor)
        else:
            self.element_click(self.Back_floor)