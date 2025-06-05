
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.contact_page import ContactPage
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_driver")
class TestContactForm:

    def is_success_alert_present(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            if "Message Sent: submitted successfully" in alert_text:
                alert.accept()
                return True
        except:
            return False
        return False

    def test_TC_CON_01_empty_fields(self):
        HomePage(self.driver, self.wait).click_contact_link()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_send_button()

        # Expect NO alert with success message
        assert not self.is_success_alert_present()

    def test_TC_CON_02_name_only(self):
            self.driver.refresh()
            contact_page = ContactPage(self.driver, self.wait)
            contact_page.click_name_field("John")
            contact_page.click_send_button()
            assert not self.is_success_alert_present()

    def test_TC_CON_03_email_only(self):
        self.driver.refresh()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_email_field("john@example.com")
        contact_page.click_send_button()
        assert not self.is_success_alert_present()

    def test_TC_CON_04_message_only(self):
        self.driver.refresh()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_message_field("Just testing.")
        contact_page.click_send_button()
        assert not self.is_success_alert_present()

    def test_TC_CON_05_name_and_email_only(self):
        self.driver.refresh()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_name_field("tino")
        contact_page.click_email_field("tino@example.com")
        contact_page.click_send_button()
        assert not self.is_success_alert_present()

    def test_TC_CON_06_name_and_message_only(self):
        self.driver.refresh()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_name_field("John")
        contact_page.click_message_field("Hello there.")
        contact_page.click_send_button()
        assert not self.is_success_alert_present()

    def test_TC_CON_07_email_and_message_only(self):
        self.driver.refresh()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_email_field("nino@example.com")
        contact_page.click_message_field("Testing!")
        contact_page.click_send_button()
        assert not self.is_success_alert_present()

    def test_TC_CON_08_valid_submission(self):
            self.driver.refresh()
            contact_page = ContactPage(self.driver, self.wait)
            contact_page.click_name_field("John Doe")
            contact_page.click_email_field("john@example.com")
            contact_page.click_subject_field("Feedback")
            contact_page.click_message_field("This is a valid message.")
            contact_page.click_send_button()
            assert self.is_success_alert_present()

    def test_TC_CON_09_invalid_email_format(self):
            self.driver.refresh()
            contact_page = ContactPage(self.driver, self.wait)
            contact_page.click_name_field("John")
            contact_page.click_email_field("john@wrong")  # Invalid format
            contact_page.click_subject_field("Bug")
            contact_page.click_message_field("Please fix this.")
            contact_page.click_send_button()
            assert  self.is_success_alert_present()

    def test_TC_CON_10_success_message_displayed(self):
        self.driver.refresh()
        contact_page = ContactPage(self.driver, self.wait)
        contact_page.click_name_field("Alice")
        contact_page.click_email_field("alice@example.com")
        contact_page.click_subject_field("Thanks")
        contact_page.click_message_field("Loved the site!")
        contact_page.click_send_button()
        assert self.is_success_alert_present()





