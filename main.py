from drivers.driver_setup import crear_driver
import time
from config.conf import *
from utils.leer_excel import *
from flows.form_flow import *
table = leer_excel(r"C:\Users\venic\Downloads\Arena RPA FormData.xlsx","Hoja 1")

if table is not None:
    # Crear el navegador (con ventana visible)
    driver = crear_driver(headless=False)
    driver.get(URL_ARENA_RPA)
    print("Título:", driver.title)
    # Llenar formulario
    run_form(driver,table,fast=True)


time.sleep(600)  # Espera para ver resultado
driver.quit()