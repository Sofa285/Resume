# Переход на страницу обратной связи и проверка заголовка
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

# Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element
def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Указываем путь к chromedriver
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://new.ruopt.com/?store_access_key=sdgd7sd7sdgsdg5hdfsdfhdf")

    
    obratnaya_svyaz = driver.find_element("xpath", "/html/body/div[1]/div[4]/div[4]/div/div[1]/div/div/div/div[1]/div/div[2]/div/ul/li[2]/a")
        #  JavaScript для прокрутки страницы к элементу
    driver.execute_script("arguments[0].scrollIntoView();", obratnaya_svyaz)
        # Действия с элементом
    obratnaya_svyaz.click()
        # Поиск и проверка попадания на страницу обратная связь
    title_text = driver.find_element("xpath", "/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/h1/span")
    if title_text.text == "Обратная связь":
            print("Элемент найден")
    else:
            print("Ошибка поиска элемента")
   
    time.sleep(5)

if __name__ == "__main__":
    first_test()

'''# авторизация и проверка заголовка страницы
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

#@pytest.fixture
def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Указываем путь к chromedriver
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get("https://new.ruopt.com/jafAJsasfasfaSAISFDa.php")

    try:
        # Поиск элементов и присваивание к переменным.
        input_username = driver.find_element("xpath", "/html/body/div[4]/div/form/div[2]/div[1]/input")
        input_password = driver.find_element("xpath", "/html/body/div[4]/div/form/div[2]/div[2]/input")
        login_button = driver.find_element("xpath", "/html/body/div[4]/div/form/div[3]/input")

        # Действия с формами
        input_username.send_keys("olennikoff@mail.ru")
        input_password.send_keys("BleH%NQR#S3#")
        login_button.click() 

        # Поиск и проверка попадания на главную страницу
        title_text = driver.find_element("xpath", "//*[@id='header_container']/div[2]/span")
        if title_text.text == "Products":
            print("Мы попали на главную страницу")
        else:
            print("Ошибка поиска элемента")
    except NoSuchElementException as e:
        print("Элемент не найден")
    finally:
        time.sleep(5)  # Задержка для просмотра результата
        #driver.quit()  # Закрыть браузер после теста

if __name__ == '__main__':
    first_test()
    #pytest.main()'''