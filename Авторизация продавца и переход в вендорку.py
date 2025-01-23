# Переход на страницу авторизации продавца, заполнение полей и отправка формы

    # Обращение к необходимым библиотекам
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

    # Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element
def test_sing_in_vendor():
    
        # Настройка драйвера chrome: исключение переключателей, отключение логгирования
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Указываем путь к chromedriver
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

        # Переход на главную страницу сайта
    driver.get("https://")

        # Поиск элемента (бургер) и присваивание переменной
    burger_button = wait_of_element_located('//*[@id="sw_dropdown_84"]/i', driver)

        # Действия с элементом
    burger_button.click()

        # Поиск элемента (кнопка входа) и присваивание переменной
    profile_button = wait_of_element_located('//*[@id="tygh_main_container"]/div[2]/div/div[1]/div/div/div/div[1]/div[4]/div/div/nav[2]/div[2]/div[2]/p/a/span', driver)

        # Ожидание пока элемент станет кликабельным
    profile_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tygh_main_container"]/div[2]/div/div[1]/div/div/div/div[1]/div[4]/div/div/nav[2]/div[2]/div[2]/p/a/span'))
)
        # Действия с элементом
    profile_button.click()

        # Поиск, ожидание и проверка открытия формы входа
    wait = WebDriverWait(driver, 10)
    title_text = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main_column_login"]/div/form/div[2]/div[1]/label')))
    if title_text.text == "E-mail:":
        print("Элемент найден")
    else:
        print("Элемент не найден")

        # Поиск элементов и присваивание к переменнным (поля для входа)
    input_email = wait_of_element_located('//*[@id="username"]', driver)
    input_password = wait_of_element_located('//*[@id="password"]', driver)
    login_button = wait_of_element_located('//*[@id="main_column_login"]/div/form/div[3]/input', driver)

        # Действия с элементами (заполнение полей)
    input_email.send_keys("sofavladimirowa@yandex.ru")
    input_password.send_keys("BleH%NQR#S3#")

        # Отправка формы
    login_button.click()

        #Поиск, ожидание и проверка перехода в вендорку
    wait = WebDriverWait(driver, 10)
    title_text = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="actions_panel"]/div/div[1]/h2')))
    if title_text.text == "Панель инструментов":
        print("Элемент найден")
    else:
        print("Элемент не найден")

        # Задержка после теста
    time.sleep(5)
        # Закрытие браузера после теста
    driver.quit()

if __name__ == "__main__":
    test_sing_in_vendor() 
