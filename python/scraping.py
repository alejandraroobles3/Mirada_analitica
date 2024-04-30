from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def main():
    # Configuración del WebDriver y opciones para ignorar las notificaciones del navegador
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Configuración de Selenium para usar ChromeDriver con las opciones definidas
    driver_path = 'C:\\Users\\aleja\\chromedriver.exe'
    driver = webdriver.Chrome(driver_path, options=chrome_options)

    try:
        driver.get('http://www.facebook.com/login')
        # Iniciar sesión en Facebook
        username = driver.find_element(By.ID, "email")
        password = driver.find_element(By.ID, "pass")
        username.send_keys("fakeporsiempre321@gmail.com")
        password.send_keys("Ale123roblesmora")
        password.send_keys(Keys.RETURN)

        # Esperar a que la página de inicio cargue completamente
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Realizar búsqueda en Facebook
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))
        search_box.send_keys('xochitl galvez')
        search_box.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]')))

        # Scroll para cargar más resultados
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Dar tiempo para que la página cargue los nuevos resultados

        # Extrae el HTML de la página y utiliza BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        posts = soup.find_all('a', href=True, attrs={'aria-label': True})

        # Filtrar enlaces de publicaciones y guardarlos en un archivo txt
        with open('links.txt', 'w') as file:
            for post in posts:
                link = post['href']
                if 'posts' in link or 'photos' in link:
                    file.write('https://www.facebook.com' + link + '\n')

    finally:
        driver.quit()

if __name__ == '__main__':
    main()
