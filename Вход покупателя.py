# Переход на страницу входа покупателя, проверка, заполнение полей и отправка формы

    # Обращение к необходимым библиотекам
from csv import writer
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
def test_sing_in():
 
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Указываем путь к chromedriver
    service = Service(r'C:/Users/bubbler/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

        # Переход на главную страницу сайта
    driver.get("https://new.ruopt.com/?store_access_key=sdgd7sd7sdgsdg5hdfsdfhdf")

        # Поиск элемента (бургер) и присваивание переменной
    burger_button = wait_of_element_located('//*[@id="sw_dropdown_84"]/i', driver)

        # Действия с элементом 
    burger_button.click()
    
        # Поиск элемента (кнопка входа) и присваивание переменной
    sign_in_button = wait_of_element_located('//*[@id="tygh_main_container"]/div[2]/div/div[1]/div/div/div/div[1]/div[4]/div/div/div[3]/div/div[2]/div/a[1]', driver)
        
        # Ожидание пока элемент станет кликабельным
    sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tygh_main_container"]/div[2]/div/div[1]/div/div/div/div[1]/div[4]/div/div/div[3]/div/div[2]/div/a[1]'))
)
        # Действия с элементом
    sign_in_button.click()
      
        # Поиск и проверка открытия формы входа
    wait = WebDriverWait(driver, 10)
    title_text = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content_main_login_tab_email"]/form/div[1]/label')))
    if title_text.text == "E-mail":
        print("Элемент найден")
    else:
        print("Ошибка поиска элемента")

        # Поиск элементов и присваивание к переменным (поля для входа)
    input_email = wait_of_element_located('//*[@id="login_main_login"]', driver)
    input_password = wait_of_element_located('//*[@id="psw_main_login"]', driver)
    login_button = wait_of_element_located('//*[@id="content_main_login_tab_email"]/form/div[3]/div[2]/button/span/bdi', driver)

        # Действия с элементами (заполнение полей)
    input_email.send_keys("olennikoff@mail.ru")
    input_password.send_keys("BleH%NQR#S3#")

        # Отправка формы
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element((By.ID, "ajax_overlay")))
    login_button.click()

        # Проверка текста во всплывающем окне после отправки формы
    wait = WebDriverWait(driver, 10)
    notification = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tygh_container"]/div[3]')))
    notification_text = notification.text
    print("Текст во всплывающем окне:", notification_text)
    expected_fragment = "Вы успешно авторизовались."
    assert expected_fragment.lower() in notification_text.lower().strip(), f"Текст не соответствует: ожидалось '{expected_fragment}', но получено '{notification_text}'"
        
        # Задержка после теста
    time.sleep(5)
        # Закрытие браузера после теста
    driver.quit()

if __name__ == "__main__":
    test_sing_in()
