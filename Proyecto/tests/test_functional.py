from selenium import webdriver
from django.test import TestCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FunctionalTest(TestCase):
    def test_login_wrong_data(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        username_input = driver.find_element(By.ID, "form2Example11")
        password_input = driver.find_element(By.ID, "form2Example22")

        username_input.send_keys("admin")
        password_input.send_keys("admin")

        login_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/section/div/div/div/div/div/div[1]/div/form/div[3]/button')))
        login_button.click()

        lista_solicitudes_button = driver.find_element(By.ID, "lista_sol")
        lista_solicitudes_button.click()
        time.sleep(2)

        boton_inicio = driver.find_element(
            By.XPATH, "/html/body/header/div/div[1]/a/img")
        boton_inicio.click()
        time.sleep(2)

        responder_solicitudes_button = driver.find_element(By.ID, "resp_sol")
        responder_solicitudes_button.click()
        time.sleep(2)

        boton_inicio = driver.find_element(
            By.XPATH, "/html/body/header/div/div[1]/a/img")
        boton_inicio.click()
        time.sleep(2)

        open311_button = driver.find_element(
            By.XPATH, "/html/body/header/div/nav/ul/a[4]/li")
        open311_button.click()
        time.sleep(2)

        boton_inicio = driver.find_element(
            By.XPATH, "/html/body/header/div/div[1]/a/img")
        boton_inicio.click()
        time.sleep(2)

        crear_solicitud_butt = driver.find_element(
            By.XPATH, "/html/body/main/section/div/div[1]/div/a")
        crear_solicitud_butt.click()
        time.sleep(2)

        boton_inicio = driver.find_element(
            By.XPATH, "/html/body/header/div/div[1]/a/img")
        boton_inicio.click()
        time.sleep(2)

        driver.quit()
