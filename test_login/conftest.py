import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Configura el navegador Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
