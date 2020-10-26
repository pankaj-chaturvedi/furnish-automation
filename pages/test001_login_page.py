import time

from pytesseract import image_to_string, pytesseract
from PIL import Image
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    google_login_button = "//div[@class='auth0-lock-social-button-text']"
    email_textfield = "//input[@id='identifierId']"
    google_next_button = "//button/div[2]"
    password_textfield = "//input[@name='password']"
    your_project_text = "//strong[contains(text(),'Your projects')]"
    user_profile_icon = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[2]/div[3]/div[1]/a[1]/span[1]"
    logout_link = "//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[4]"

    # Relogin test locators for google.
    cache_login = "//div[@id='profileIdentifier']"
    another_user = "//div[@class='BHzsHc']"

    # wrong password entered
    invalid_login_validation = "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div[2]/span" #//span[contains(text(),'Wrong password. Try again or click Forgot password to reset it.')]

    # Google captcha image and textfield path
    captacha_path = "//img[@id='captchaimg']"
    welcome_text = "//span[contains(text(),'Welcome')]"
    captach_field= "//input[@id='ca']"

    def click_google_login_button(self):
        """Click on google login button"""
        self.wait_for_element(self.google_login_button)
        self.element_click(self.google_login_button)

    def enter_email(self, email):
        """Enter email"""
        self.send_keys(email, self.email_textfield)

    def click_google_next_button(self):
        """Click on google page next button"""
        self.element_click(self.google_next_button)

    def enter_password(self, password):
        """Enter user password"""
        self.send_keys(password, self.password_textfield)

    def click_user_profile_icon(self):
        """Click on user profile icon on furnish home page"""
        time.sleep(5)
        self.element_click(self.user_profile_icon)

    def click_logout_link(self):
        """Click on logout icon"""
        time.sleep(2)
        self.element_click(self.logout_link)

    def click_cache(self):
        self.element_click(self.cache_login)

    def another_user_login(self):
        self.element_click(self.another_user)

    def validation_message(self):
        self.element_click(self.invalid_login_validation)

    # def get_captcha_text(self, location, size):
    #     pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    #     im = Image.open('screenshot.png')  # uses PIL library to open image in memory
    #
    #     left = location['x']
    #     top = location['y']
    #     right = location['x'] + size['width']
    #     bottom = location['y'] + size['height']
    #
    #     im = im.crop((left, top, right, bottom))  # defines crop points
    #     im.save('screenshot.png')
    #     captcha_text = image_to_string(Image.open('screenshot.png'))
    #     return captcha_text

    def login_to_website(self, email="", password=""):
        """User is able to login on Gmail account successfully.."""
        self.click_google_login_button()
        time.sleep(2)
        self.enter_email(email)
        time.sleep(2)
        self.click_google_next_button()
        time.sleep(2)
        self.enter_password(password)
        time.sleep(2)
        self.click_google_next_button()
        time.sleep(2)
        # text = 'Welcome'
        # if self.get_text(self.welcome_text) == text:
        #     element = self.get_element(self.captacha_path)  # find part of the page you want image of
        #     location = element.location
        #     size = element.size
        #     self.screenShot('screenshot.png')
        #     captcha = self.get_element(self.captach_field)
        #     captcha_text = self.get_captcha_text(location, size)
        #     self.element_click(captcha)
        #     self.send_keys(captcha_text)
        #     self.enter_password(password)
        #     time.sleep(2)
        #     self.click_next_button()
        # else:
        #     self.log.info('Login successfully!!!')

    def verify_login_successfully(self):
        """Verify your project text after user logged in."""
        time.sleep(2)
        expected_text = "Your projects"
        actual_text = self.get_text(self.your_project_text)
        self.verify_text_match(actual_text=actual_text, expected_text=expected_text)

    def login_with_invalid_credentials(self, email="", password=""):
        """User is not able to login entering invalid credentials"""
        self.enter_email(email)
        time.sleep(2)
        self.click_google_next_button()
        time.sleep(2)
        self.enter_password(password)
        time.sleep(2)
        self.click_google_next_button()

    def verify_invalid_login_validation_message(self):
        """Verify validation message whe user try to login with invalid credentials"""
        validation_text= "Wrong password. Try again or click Forgot password to reset it."
        message = self.get_text(self.invalid_login_validation)
        self.verify_text_match(actual_text=message, expected_text=validation_text)

    def login_same_user_with_cache(self):
        """Login user again using self google cookies option"""
        self.click_google_login_button()
        time.sleep(2)
        self.click_cache()

    def anotherUser(self):
        """login user using google another option"""
        self.click_google_login_button()
        time.sleep(2)
        self.another_user_login()

    def logout(self):
        """User is able to logout after clicking on logout link"""
        time.sleep(5)
        self.click_user_profile_icon()
        self.click_logout_link()
