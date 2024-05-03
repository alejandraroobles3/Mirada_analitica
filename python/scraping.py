from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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
driver.get('https://www.facebook.com/ClaudDelgadillo')

# Scroll through the page 10 times
for _ in range(100):
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # wait to load page

# Extract hrefs using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
links = soup.find_all('span', class_='x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j')

# We need to find <a> elements within these <span> elements
hrefs = [a['href'] for link in links for a in link.find_all('a') if a.get('href') and a['href'].startswith('https')]
print(f"Total hrefs found: {len(hrefs)}")

trimmed_links = [link.split('?')[0] for link in hrefs]

# Imprimir los enlaces recortados
for trimmed_link in trimmed_links:
    print(trimmed_link)

with open('txt/links.txt', 'a', encoding='utf-8') as file:
    for item in trimmed_links:
        file.write(item+ '\n')
# Cerrar el navegador
driver.quit()


