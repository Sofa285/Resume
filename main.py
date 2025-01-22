'''# проверка наличия поля user-name на странице
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Указываем путь к chromedriver
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.saucedemo.com/")

    try:
        input_username = driver.find_element("id", "user-name")
        print("Элемент найден")
    except NoSuchElementException:
        print("Элемент не найден")



if __name__ == "__main__":
    first_test()'''

'''# авторизация и проверка заголовка страницы
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Указываем путь к chromedriver
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get("https://www.saucedemo.com/")

    try:
        # Поиск элементов и присваивание к переменным.
        input_username = driver.find_element("xpath", "//*[@id='user-name']")
        input_password = driver.find_element("xpath", "//*[@id='password']")
        login_button = driver.find_element("xpath", "//*[@id='login-button']")

        # Действия с формами
        input_username.send_keys("standard_user")
        input_password.send_keys("secret_sauce")
        login_button.click()  # Используем click() вместо send_keys(Keys.RETURN)

        # Поиск и проверка попадания на главную страницу
        title_text = driver.find_element("xpath", "//*[@id='header_container']/div[2]/span")
        if title_text.text == "Products":
            print("Мы попали на главную страницу")
        else:
            print("Ошибка поиска элемента")
    except NoSuchElementException as e:
        print(f"Элемент не найден: {e}")
    finally:
        time.sleep(5)  # Задержка для просмотра результата
        driver.quit()  # Закрыть браузер после теста

if __name__ == '__main__':
    first_test()'''

# авторизация и добавление товара в корзину и проверка добавленного товара в корзине
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service  # Добавлен импорт Service
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

def test_add_jacket_to_the_shopcart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Убедитесь, что путь к chromedriver указан правильно
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get("https://www.saucedemo.com/")

    # Поиск и ожидание элементов и присваивание к переменным.
    input_username = wait_of_element_located('//*[@id="user-name"]', driver)
    input_password = wait_of_element_located('//*[@id="password"]', driver)
    login_button = wait_of_element_located('//*[@id="login-button"]', driver)

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.click()  # Изменено с send_keys(Keys.RETURN) на click()

    # Поиск и ожидание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located('//*[@id="item_5_title_link"]/div', driver)
    item_name.click()

    # Поиск и ожидание кнопки добавления товара и клик по этой кнопке
    item_add_button = wait_of_element_located('//*[@id="add-to-cart"]', driver)
    item_add_button.click()

    # Ждем пока товар добавится в корзину, появится span(кол-во позиций в корзине) и кликаем по корзине чтобы перейти
    wait_of_element_located('//*[@id="shopping_cart_container"]/a/span', driver).click()

    # Еще один поиск ссылки элемента позиции магазина
    item_name = wait_of_element_located('//*[@id="item_5_title_link"]/div', driver)
    if item_name.text == "Sauce Labs Fleece Jacket":
        print("Товар присутствует в корзине")
    else:
        print("Товар отсутствует")

    time.sleep(5)
    driver.quit()  # Закрытие браузера после завершения теста

if __name__ == '__main__':
    test_add_jacket_to_the_shopcart()

'''import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# Функция ожидания элементов
def wait_of_element_located(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element

# Вынесем инициализацию драйвера в отдельную фикстуру pytest
@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver.get("https://www.saucedemo.com/")
    yield driver
    #driver.quit()  # Закрываем драйвер после завершения теста

# Вынесем аутентификацию юзера в отдельную функцию
def auth_user(driver_init):
    input_username = wait_of_element_located('//*[@id="user-name"]', driver_init)
    input_password = wait_of_element_located('//*[@id="password"]', driver_init)
    login_button = wait_of_element_located('//*[@id="login-button"]', driver_init)

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.click()

def add_item_to_cart(driver_init):
    # Поиск и ожидание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located('//*[@id="item_5_title_link"]/div', driver_init)
    item_name.click()

    # Поиск и ожидание кнопки добавления товара и клик по этой кнопке
    item_add_button = wait_of_element_located('//*[@id="add-to-cart"]', driver_init)
    item_add_button.click()

    # Ждем пока товар добавится в корзину, появится span(кол-во позиций в корзине)
    shop_cart_with_item = wait_of_element_located('//*[@id="shopping_cart_container"]/a/span', driver_init)
    return shop_cart_with_item

def test_add_jacket_to_the_shopcart(driver_init):
    # Аутентификация пользователя
    auth_user(driver_init)

    # Добавление товара в корзину
    add_item_to_cart(driver_init)

    # Поиск корзины и клик
    wait_of_element_located('//*[@id="shopping_cart_container"]/a', driver_init).click()

    # Поиск ссылки элемента позиции магазина
    item_name = wait_of_element_located('//*[@id="item_5_title_link"]/div', driver_init)

    # Поиск описания товара
    item_description = wait_of_element_located('//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[1]', driver_init)

    assert item_name.text == "Sauce Labs Fleece Jacket"
    assert item_description.text == "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office."
    
        # Еще один поиск ссылки элемента позиции магазина
    item_name = wait_of_element_located('//*[@id="item_5_title_link"]/div', driver_init)
    if item_name.text == "Sauce Labs Fleece Jacket":
        print("Товар присутствует в корзине")
    else:
        print("Товар отсутствует")

    time.sleep(5)
    driver.quit()
if __name__ == '__main__':
    pytest.main()'''