import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Importar Service
from webdriver_manager.chrome import ChromeDriverManager  # Para manejar automáticamente el chromedriver
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Usando Service para especificar el chromedriver
        service = Service(ChromeDriverManager().install())  # Esto instalará y configurará automáticamente el chromedriver
        self.driver = webdriver.Chrome(service=service)  # Usar el servicio para iniciar Chrome
        self.driver.get("http://localhost:8000/index.html")  # URL de la página de inicio de sesión
    
    def test_login_success(self):
        driver = self.driver
        driver.get("http://localhost:8000/index.html")
        
        # Esperar a que la página cargue completamente
        time.sleep(2)

        # Buscar los campos de texto y el botón de inicio de sesión
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        # Ingresar credenciales válidas
        username_field.send_keys("usuario_valido")
        password_field.send_keys("contraseña_valida")
        login_button.click()

        # Esperar a que la página de inicio se cargue
        time.sleep(3)

        # Verificar que el usuario ha iniciado sesión (esto depende de tu página, ajusta según sea necesario)
        self.assertIn("Bienvenido", driver.page_source)

    def test_login_invalid_credentials(self):
        driver = self.driver
        driver.get("http://localhost:8000/index.html")
        
        # Esperar a que la página cargue completamente
        time.sleep(2)

        # Buscar los campos de texto y el botón de inicio de sesión
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        # Ingresar credenciales inválidas
        username_field.send_keys("usuario_invalido")
        password_field.send_keys("contraseña_incorrecta")
        login_button.click()

        # Esperar un poco para ver el mensaje de error
        time.sleep(3)

        # Verificar que aparece un mensaje de error (ajusta esto según tu implementación)
        self.assertIn("Credenciales incorrectas", driver.page_source)

    def test_login_empty_fields(self):
        driver = self.driver
        driver.get("http://localhost:8000/index.html")
        
        # Esperar a que la página cargue completamente
        time.sleep(2)

        # Buscar el botón de inicio de sesión (no es necesario rellenar los campos)
        login_button = driver.find_element(By.ID, "loginButton")
        login_button.click()

        # Esperar un poco para ver si muestra el mensaje de error
        time.sleep(3)

        # Verificar que aparece un mensaje de error si los campos están vacíos
        self.assertIn("Por favor complete todos los campos", driver.page_source)

    def tearDown(self):
        # Cerrar el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
