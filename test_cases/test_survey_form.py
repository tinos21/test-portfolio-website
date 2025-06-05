from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.survey_page import SurveyPage


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

    def test_TC_SUR_01_valid_submission(self):
        HomePage(self.driver, self.wait).click_survey_link()
        page = SurveyPage(self.driver, self.wait)
        page.click_name_field("Tino")
        page.click_email_field("tino@example.com")
        page.click_feedback_field("Great experience.")
        page.click_submit_button()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        assert "Survey Response: Survey submitted successfully" in alert_text
        alert.accept()


    def test_TC_SUR_02_missing_required_fields(self):
        page = SurveyPage(self.driver, self.wait)
        page.click_name_field("")  # Missing name
        page.click_email_field("")  # Missing email
        page.click_feedback_field("Feedback test ")
        page.click_submit_button()

        assert not self.is_success_alert_present()

    def test_TC_SUR_03_validation_messages(self):
        page = SurveyPage(self.driver, self.wait)
        page.click_submit_button()
        assert not self.is_success_alert_present()
        # or locate specific error span

    def test_TC_SUR_04_max_character_input(self):
        self.driver.refresh()
        page = SurveyPage(self.driver, self.wait)
        long_text = "a" * 1000
        page.click_name_field(long_text)
        page.click_email_field("tino@example.com")
        page.click_feedback_field(long_text)
        page.click_submit_button()

        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            assert "Survey Response: Survey submitted successfully" not in alert_text, "Form incorrectly accepted long input"
        except TimeoutException:
            # No alert appeared, which is expected in a negative test
            assert True

    def test_TC_SUR_05_special_characters_input(self):
        self.driver.refresh()
        page = SurveyPage(self.driver, self.wait)
        special_text = "@#$%^&*()_+~`"
        page.click_name_field(special_text)
        page.click_email_field("invalid@input.com")
        page.click_feedback_field(special_text)
        page.click_submit_button()

        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            assert "Survey Response: Survey submitted successfully" not in alert_text, "Form incorrectly accepted "
        except TimeoutException:
            # No alert appeared, which is expected in a negative test
            assert True

    def test_TC_SUR_06_trimmed_input(self):
        self.driver.refresh()
        page = SurveyPage(self.driver, self.wait)
        page.click_name_field("   Tino   ")
        page.click_email_field("   tino@example.com   ")
        page.click_feedback_field("   Great job   ")
        page.click_submit_button()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        assert "Survey Response: Survey submitted successfully" in alert_text
        alert.accept()

    def test_TC_SUR_07_invalid_email_format(self):
        self.driver.refresh()
        page = SurveyPage(self.driver, self.wait)
        page.click_name_field("Tino")
        page.click_email_field("invalid-email")
        page.click_feedback_field("Good stuff.")
        page.click_submit_button()

        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            assert "Survey Response: Survey submitted successfully" not in alert_text, "Form incorrectly accepted "
        except TimeoutException:
            # No alert appeared, which is expected in a negative test
            assert True



    def test_TC_SUR_09_success_toast_or_redirect(self):
        self.driver.refresh()
        page = SurveyPage(self.driver, self.wait)
        page.click_name_field("Tino")
        page.click_email_field("tino@example.com")
        page.click_feedback_field("Looks great.")
        page.click_submit_button()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        assert "Survey Response: Survey submitted successfully" in alert_text
        alert.accept()


    def test_TC_SUR_10_only_feedback_field_filled(self):
        self.driver.refresh()
        page = SurveyPage(self.driver, self.wait)
        page.click_name_field("")
        page.click_email_field("")
        page.click_feedback_field("Only feedback.")
        page.click_submit_button()

        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            assert "Survey Response: Survey submitted successfully" not in alert_text, "Form incorrectly accepted "
        except TimeoutException:
            # No alert appeared, which is expected in a negative test
            assert True

