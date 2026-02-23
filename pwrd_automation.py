from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep


def automation_check(pwrd):
    try:
        service = Service('./geckodriver')
        firefox_instance = webdriver.Firefox(service=service)
        firefox_instance.get('https://haveibeenpwned.com/Passwords')
        input_field = firefox_instance.find_element(By.ID, "passwordInput")
        input_field.send_keys(pwrd)
        check_btn = firefox_instance.find_element(By.ID, 'checkButton')
        check_btn.click()
        sleep(2)
        result_h3 = firefox_instance.find_element(
            By.CSS_SELECTOR, "h3.fw-bold.mb-3")
        if result_h3.text.find("Good") != -1:
            result_p = firefox_instance.find_element(
                By.CSS_SELECTOR, "div.alert.alert-success.p-4.text-center.mb-4 p.mb-0")
            final_result_text = result_h3.text + "\n" + result_p.text
        else:
            result_h3 = firefox_instance.find_element(
                By.CSS_SELECTOR, "div.alert.alert-danger.p-4.text-center.mb-5 h3.fw-bold.mb-3")
            result_p1 = firefox_instance.find_element(
                By.CSS_SELECTOR, "div.alert.alert-danger.p-4.text-center.mb-5 p.mb-3")
            result_p2 = firefox_instance.find_element(
                By.CSS_SELECTOR, "div.alert.alert-danger.p-4.text-center.mb-5 p.mb-0")
            final_result_text = result_h3.text + "\n" + \
                result_p1.text + "\n" + result_p2.text
        firefox_instance.quit()
        firefox_instance.quit()
        print("PCA: DONE!")
        return final_result_text
    except:
        raise Exception("something went wrong during automation!")
