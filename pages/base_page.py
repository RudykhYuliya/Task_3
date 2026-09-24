from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.header_locators import HeaderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    def set_value(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', field)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_url_contains(self, part):
        self.wait.until(EC.url_contains(part))

    def wait_url_is(self, url):
        self.wait.until(lambda driver: driver.current_url.rstrip('/') == url.rstrip('/'))

    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_class(self, locator, class_name):
        self.wait.until(
            lambda driver: class_name in driver.find_element(*locator).get_attribute('class')
        )

    def wait_text_changes(self, locator, previous):
        self.wait.until(lambda driver: driver.find_element(*locator).text != previous)
        return self.get_text(locator)

    def wait_number_greater_than(self, locator, previous):
        self.wait.until(lambda driver: int(driver.find_element(*locator).text) > previous)

    def wait_digits(self, locator):
        self.wait.until(lambda driver: driver.find_element(*locator).text.strip().isdigit())
        return self.get_text(locator).strip()

    def wait_order_number(self, locator):
        self.wait.until(
            lambda driver: (
                driver.find_element(*locator).text.strip().isdigit()
                and driver.find_element(*locator).text.strip() != '9999'
            )
        )
        return self.get_text(locator).strip()

    def script_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        self.driver.execute_script('arguments[0].click();', element)

    def drag_and_drop(self, source, target):
        source_element = self.wait.until(EC.visibility_of_element_located(source))
        target_element = self.wait.until(EC.visibility_of_element_located(target))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', source_element)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            const fire = (element, type) => {
                element.dispatchEvent(new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                }));
            };
            fire(source, 'dragstart');
            fire(target, 'dragenter');
            fire(target, 'dragover');
            fire(target, 'drop');
            fire(source, 'dragend');
            """,
            source_element,
            target_element,
        )

    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR)

    def click_order_feed(self):
        self.click(HeaderLocators.ORDER_FEED)

    def click_account(self):
        self.click(HeaderLocators.ACCOUNT)
