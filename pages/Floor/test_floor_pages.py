import time
from selenium.webdriver.common.keys import Keys

from base.selenium_driver import SeleniumDriver

class Floor_Plan(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Your_project = "//*[@id='main-container']/main/div/div/div/div[2]/div[1]/div[2]/div"
    #Back = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[1]/div"
    Floor_Plan = "//*[@id='root']/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/a/div/div"

    def Floor_plan_Navigation(self):
        time.sleep(2)
        self.element_click(self.Your_project)
        time.sleep(2)
        self.element_click(self.Floor_Plan)
        time.sleep(2)
