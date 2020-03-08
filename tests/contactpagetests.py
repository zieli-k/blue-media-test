__author__ = "Karol Zieliński"
import unittest
from time import sleep

from selenium import webdriver

from enums import ContactPageEnums
from env_config import Config as EnviromentConfig
from data_config import Config as DataConfig
from pages.pages import ContactPage


class ContactPageTest(unittest.TestCase):
    ENV = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = EnviromentConfig(self.ENV).get_url()
        self.pages = ContactPage(self.driver)
        self.data = DataConfig(__class__.__name__).get_config()
        self.enums = ContactPageEnums

    def test_fill_contact_form(self):
        self.driver.get(self.url)
        assert self.driver.title == "Kontakt - Bluemedia"
        self.pages.chose_client_type()
        self.pages.type_name(self.data[self.enums.DataTypes.CorrectData.value][self.enums.Data.Name.value])
        self.pages.type_email(self.data[self.enums.DataTypes.CorrectData.value][self.enums.Data.Email.value])
        self.pages.type_phone(self.data[self.enums.DataTypes.CorrectData.value][self.enums.Data.Phone.value])
        self.pages.chose_subject(self.data[self.enums.DataTypes.CorrectData.value][self.enums.Data.Subject.value])
        self.pages.type_content(self.data[self.enums.DataTypes.CorrectData.value][self.enums.Data.Content.value])
        self.pages.sign_agreement()
        self.pages.sign_email_respond()
        sleep(60)
