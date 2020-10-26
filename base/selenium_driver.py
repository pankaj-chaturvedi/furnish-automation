import datetime
import os
import logging
import time
import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from PIL import Image


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")

    def get_title(self):
        """Get title of the page"""
        try:
            return self.driver.title
        except:
            self.log.info("Title not found")
            raise

    def get_by_type(self, locatorType):
        """Get element by its type."""
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def get_element(self, locator, locatorType="xpath"):
        """
        Get element name
        locator: "It can be id, xpath, css_selector etc.."
        locatorType: by default its xpath.
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def get_element_list(self, locator, locatorType="xpath"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def element_click(self, locator="", locatorType="xpath", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
                assert element is not None, (
                        "Locator not found. Cannot click on the element with locator: " + locator +
                        "locatorType: " + locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Locator not found. Cannot click on the element with locator: " + locator +
                          "locatorType: " + locatorType)

    def send_keys(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
                assert element is not None, (
                        "locator not found. Cannot send data on the element with locator: " + locator +
                        " locatorType: " + locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            raise

    def clear_field(self, locator="", locatorType="xpath"):
        """
        Clear an element field
        """
        element = self.get_element(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def get_text(self, locator="", locatorType="xpath", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
                assert element is not None, ("Locator not found. Failed to get text on element " + info)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def is_element_present(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
                assert element is None, ("Locator not found. Element not present with locator: " + locator +
                                         " locatorType: " + locatorType)
                return False
            else:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator="", locatorType="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locatorType="xpath",
                         timeout=10, pollFrequency=1):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            assert element is not None, ("Element not present with locator: " + locator +
                                         " locatorType: " + locatorType)
            self.log.info("Element appeared on the web page")
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def web_scroll(self, direction="up"):
        """
        To scroll the web page up and down
        """
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert expected_text.lower() in actual_text.lower(), (
                    f"Actual text mismatched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.screenShot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text contain expected text.")

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify actual text match with the expected text.

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert expected_text.lower() == actual_text.lower(), (
                    f"Actual text mismatched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.screenShot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text matched with the expected text.")

    def fullpage_screenshot(self, file):
        print("Starting chrome full page screenshot workaround ...")

        total_width = self.driver.execute_script("return document.body.offsetWidth")
        total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = self.driver.execute_script("return document.body.clientWidth")
        viewport_height = self.driver.execute_script("return window.innerHeight")
        print(
            "Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height, viewport_width, viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                self.driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                #self.driver.execute_script("document.getElementsByClassName('Toastify').setAttribute('style', 'position: absolute; top: 0px;');")
                print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            print("Capturing {0} ...".format(file_name))

            self.driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            print("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(file)
        print("Finishing chrome full page screenshot workaround...")
        return True
