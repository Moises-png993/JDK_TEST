from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
class ClientsPage(BasePage):

    TITLE = (By.XPATH, "//h1[text()='Clientes']")
    NEW_CLIENT_BUTTON = (
        By.XPATH,
        "//button[.//span[contains(text(),'Nuevo Cliente')]]"
    )
    POP_UP_IMPORTANT_MESSAGE = (
        By.XPATH,
        "//h2[contains(., 'Importante:')]"
        )
    PERSONA_NATURAL_RADIO = (
        By.XPATH,
        "//label[.//span[normalize-space()='Persona Natural']]"
    )

    DOCUMENT_TYPE_SELECT = (
        By.XPATH,
        "//input[@id='general_info_document_type']/ancestor::div[contains(@class,'ant-select')]"
    )

    DOCUMENT_NUMBER_INPUT = (
        By.ID,
        "general_info_document_number"
    )

    NAME_INPUT = (
        By.ID,
        "general_info_name"
    )

    LAST_NAME_INPUT = (
        By.ID,
        "general_info_last_name"
    )

    CLIENT_NUMBER_INPUT = (
        By.ID,
        "general_info_number_client"
    )
    EMAIL_INPUT = (
        By.ID,
        "general_info_email"
    )

    PHONE_INPUT = (
        By.ID,
        "general_info_phone"
    )

    MOBILE_INPUT = (
        By.ID,
        "general_info_mobile"
    )

    DEPARTMENT_SELECT = (
        By.XPATH,
        "//input[@id='address_catMhDepartamentoId']/ancestor::div[@class='ant-select-selector']"
    )

    MUNICIPALITY_SELECT = (
        By.XPATH,
        "//input[@id='address_catMhMunicipioId']/ancestor::div[@class='ant-select-selector']"
    )

    DISTRICT_SELECT = (
        By.XPATH,
        "//input[@id='address_district']/ancestor::div[@class='ant-select-selector']"
    )
    STREET_INPUT = (
        By.ID,
        "address_street"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and .//span[normalize-space()='Guardar']]"
    )

    MODAL = (By.CLASS_NAME, "ant-modal")

    def is_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        ).is_displayed()
    
    def click_new_client(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.NEW_CLIENT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_new_client_modal_open(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.POP_UP_IMPORTANT_MESSAGE)
        ).is_displayed()
    
    def select_persona_natural(self):
        radio = self.wait.until(
            EC.element_to_be_clickable(self.PERSONA_NATURAL_RADIO)
        )
        radio.click()

    def open_document_type_select(self):
        select = self.wait.until(
            EC.element_to_be_clickable(self.DOCUMENT_TYPE_SELECT)
        )
        select.click()
    
    def select_document_type(self, option_text):
        self.open_document_type_select()

        option = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[contains(@class,'ant-select-item-option') and .//span[normalize-space()='{option_text}'] or normalize-space()='{option_text}']"
            ))
        )
        option.click()

    def enter_document_number(self, number):
        input_field = self.wait.until(
            EC.visibility_of_element_located(self.DOCUMENT_NUMBER_INPUT)
        )
        input_field.clear()
        input_field.send_keys(number)

    def enter_name(self, name):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.NAME_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(name)

    def enter_last_name(self, last_name):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(last_name)
    
    def enter_client_number(self, number):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.CLIENT_NUMBER_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(str(number))
    
    def enter_email(self, email):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.EMAIL_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(email)

    def enter_phone(self, phone):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.PHONE_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(phone)
    
    def enter_mobile(self, mobile):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.MOBILE_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(mobile)

    def select_department(self, department_name):
        select = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//input[@id='address_catMhDepartamentoId']/ancestor::div[@class='ant-select-selector']"
            ))
        )
        select.click()

        option = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[contains(@class,'ant-select-dropdown') and not(contains(@class,'ant-select-dropdown-hidden'))]"
                f"//div[contains(@class,'ant-select-item-option') and @title='{department_name}']"
            ))
        )
        self.driver.execute_script("arguments[0].click();", option)
        
        self.wait.until(
            EC.invisibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'ant-select-dropdown') and not(contains(@class,'ant-select-dropdown-hidden'))]"
            ))
        )
        
    def select_municipality(self, municipality_name):
        trigger = self.wait.until(
            EC.element_to_be_clickable(self.MUNICIPALITY_SELECT)
        )
        trigger.click()

        option = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[contains(@class,'ant-select-dropdown') and not(contains(@class,'ant-select-dropdown-hidden'))]"
                f"//div[contains(@class,'ant-select-item-option') and @title='{municipality_name}']"
            ))
        )
        self.driver.execute_script("arguments[0].click();", option)

        self.wait.until(
            EC.invisibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'ant-select-dropdown') and not(contains(@class,'ant-select-dropdown-hidden'))]"
            ))
        )

    def select_district(self, district_name):
        trigger = self.wait.until(
            EC.element_to_be_clickable(self.DISTRICT_SELECT)
        )
        trigger.click()

        option = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[contains(@class,'ant-select-dropdown') and not(contains(@class,'ant-select-dropdown-hidden'))]"
                f"//div[contains(@class,'ant-select-item-option') and @title='{district_name}']"
            ))
        )
        self.driver.execute_script("arguments[0].click();", option)

        self.wait.until(
            EC.invisibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'ant-select-dropdown') and not(contains(@class,'ant-select-dropdown-hidden'))]"
            ))
        )
   
    def enter_street(self, street):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.STREET_INPUT)
        )
        input_field.send_keys(Keys.CONTROL + "a")
        input_field.send_keys(Keys.DELETE)
        input_field.send_keys(street)

    def click_save(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        button.click()

    def wait_modal_to_close(self):
        self.wait.until(
            EC.invisibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'ant-modal') and contains(@class,'ant-modal-open')]"
            ))
        )

    def create_client(self, data):

        self.click_new_client()
        self.wait.until(
            EC.visibility_of_element_located(self.POP_UP_IMPORTANT_MESSAGE)
        )
        self.select_persona_natural()
        self.select_document_type(data["document_type"])
        self.enter_document_number(data["document_number"])
        self.enter_name(data["name"])
        self.enter_last_name(data["last_name"])
        self.enter_client_number(data["client_number"])
        self.enter_email(data["email"])
        self.enter_phone(data["phone"])
        self.enter_mobile(data["mobile"])

        self.select_department(data["department"])
        
        self.select_municipality(data["municipality"])
        self.select_district(data["district"])

        self.enter_street(data["street"])

        self.click_save()
        self.wait_modal_to_close()