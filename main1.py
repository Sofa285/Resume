# Переход на страницу обратной связи и проверка, заполнение полей
from csv import writer
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
        # Поиск и ожидание элементов и присваивание к переменным
    input_email = wait_of_element_located('/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/input[2]', driver)
    input_name = wait_of_element_located('/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/div/div/div[2]/form/div[2]/input', driver)
    input_topic = wait_of_element_located('/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/div/div/div[2]/form/div[3]/input', driver)
    input_message = wait_of_element_located('/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/div/div/div[2]/form/div[4]/textarea', driver)
    send_button = wait_of_element_located('/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/div/div/div[2]/form/div[5]/button', driver)
        #  JavaScript для прокрутки страницы к элементу
    driver.execute_script("arguments[0].scrollIntoView();", send_button)
        # Действия с формами
        # Заполнение формы
    input_email.send_keys("test@mail.ru")
    input_name.send_keys("Тест")
    input_topic.send_keys("Тест")
    input_message.send_keys("Тест")
        # Отправка формы
    send_button.click()
        # Поиск и проверка попадания на страницу после отправки формы обратной связи
    title_text = driver.find_element("xpath", "/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div/div/div/div/p[2]")
    if title_text.text == "Благодарим вас за обращение к нам。Мы ответим вам при первой же возможности。":
            print("Элемент найден")
    else:
            print("Ошибка поиска элемента")

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    first_test()
   