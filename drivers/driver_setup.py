from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def crear_driver(headless=False):
    options = Options()

    if headless:
        # Headless moderno (más compatible con UI actual)
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    # Argumentos adicionales para mejorar compatibilidad y estabilidad
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--lang=es-ES")

    # Crear el servicio usando webdriver-manager
    service = Service(ChromeDriverManager().install())

    # Inicializar el navegador
    driver = webdriver.Chrome(service=service, options=options)
    return driver
