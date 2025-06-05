from selenium.webdriver.common.by import By

class ContactPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_name_field(self, namevalue):
        namefield = self.driver.find_element(By.ID, "name")
        namefield.clear()
        namefield.send_keys(namevalue)

    def click_email_field(self, emailvalue):
        emailfield = self.driver.find_element(By.ID, "email")
        emailfield.clear()
        emailfield.send_keys(emailvalue)

    def click_subject_field(self, subjectvalue):
        subjectfield = self.driver.find_element(By.ID, "subject")
        subjectfield.clear()
        subjectfield.send_keys(subjectvalue)

    def click_message_field(self, messagevalue):
        messagefield = self.driver.find_element(By.ID, "message")
        messagefield.clear()
        messagefield.send_keys(messagevalue)

    def click_send_button(self):
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Send'])[1]").click()
