from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_survey_link(self):
        self.driver.find_element(By.ID, 'surveypage').click()

    def click_contact_link(self):
        self.driver.find_element(By.ID, 'contactpage').click()



