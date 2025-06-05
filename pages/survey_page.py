from selenium.webdriver.common.by import By


class SurveyPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_name_field(self,username_value):
        name = self.driver.find_element(By.ID, 'name')
        name.clear()
        name.send_keys(username_value)

    def click_email_field(self, email_value):
        email = self.driver.find_element(By.ID, 'email')
        email.clear()
        email.send_keys(email_value)

    def click_feedback_field(self, feedback_value):
        feedback = self.driver.find_element(By.ID, 'feedback')
        feedback.clear()
        feedback.send_keys(feedback_value)

    def click_submit_button(self):
        self.driver.find_element(By.ID, 'submit-button').click()






