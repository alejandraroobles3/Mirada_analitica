from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
import time

# Opciones para ignorar las notificaciones del navegador
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Configuración de Selenium para usar ChromeDriver con las opciones definidas
driver_path = 'C:\\Users\\aleja\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=chrome_options)
driver.get('https://www.facebook.com/')

# Iniciar sesión en Facebook
username = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

username.send_keys("fakeporsiempre321@gmail.com")
password.send_keys("Ale123roblesmora")
password.send_keys(Keys.RETURN)

# Esperar a que la página cargue
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Navegar a la publicación específica
driver.get('https://www.facebook.com/ClaudiaSheinbaumPardo/posts/pfbid024AbxMPP3kbin7L2RGysNczgkJHS76dqL3hFjHta2rsAQhv5M4B1NvxqJr94xdbL6l')

# Expandir todos los comentarios
while True:
    try:
        # Primero hacemos clic en el div inicial para abrir opciones (si es necesario)
        initial_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.x78zum5.x1w0mnb.xeuugli'))
        )
        initial_div.click()
        driver.execute_script("arguments[0].scrollIntoView();", initial_div)
        time.sleep(5)  # Pequeña pausa para asegurar que el segundo div sea interactuable
        
    except:
        break

# Extraer los comentarios usando BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Asegúrate de actualizar el selector aquí para coincidir con los comentarios específicos
comments = soup.find_all('div', class_='x1lliihq xjkvuk6 x1iorvi4')

print(f"Total de comentarios extraídos : {len(comments)}")
for comment in comments:
    print(comment.text.strip())

with open('txt/claudia.txt', 'a', encoding='utf-8') as file:
    for item in comments:
        file.write(item.text.strip() + '\n')
# Cerrar el navegador
driver.quit()

