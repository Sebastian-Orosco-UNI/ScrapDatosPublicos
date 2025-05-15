from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os

# Configuración del navegador
options = Options()
options.add_argument("--headless=new")  # Modo sin cabeza
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Inicializar el driver usando webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Abrir la página
driver.get('https://www.sbs.gob.pe/app/pp/EstadisticasSAEEPortal/Paginas/TIActivaMercado.aspx?tip=B')
wait = WebDriverWait(driver, 10)

# Establecer fecha
nueva_fecha = '02/05/2024'
fecha_input = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_cphContent_rdpDate_dateInput')))
fecha_input.clear()
fecha_input.send_keys(nueva_fecha)

# Hacer clic en Consultar
boton_consultar = wait.until(EC.element_to_be_clickable((By.ID, 'ctl00_cphContent_btnConsultar')))
boton_consultar.click()
time.sleep(2)

# IDs a consultar
ids = {
    "TAMN": 'ctl00_cphContent_lblVAL_TAMN_TASA',
    "TAMN1": 'ctl00_cphContent_lblVAL_TAMN_M1_TASA',
    "TAMN2": 'ctl00_cphContent_lblVAL_TAMN_M2_TASA',
    "TAMEX": 'ctl00_cphContent_lblVAL_TAMEX_TASA',
    "fecha_input": 'ctl00_cphContent_rdpDate_dateInput'
}

# Obtener fecha real desde la página
fecha_input = wait.until(EC.presence_of_element_located((By.ID, ids['fecha_input'])))
fecha_consulta = fecha_input.get_attribute('value')
dia, mes, anio = fecha_consulta.split('/')
fecha_consulta_f = f"{anio}-{mes}-{dia}"

# Obtener valores
TAMN = wait.until(EC.visibility_of_element_located((By.ID, ids['TAMN']))).text
TAMN1 = driver.find_element(By.ID, ids['TAMN1']).text
TAMN2 = driver.find_element(By.ID, ids['TAMN2']).text
TAMEX = driver.find_element(By.ID, ids['TAMEX']).text
driver.quit()

# Crear DataFrame
data = [
    [fecha_consulta_f, 'Moneda Nacional (TAMN)', TAMN, 'porcentaje', 'anual', 'SBS'],
    [fecha_consulta_f, 'Moneda Nacional (TAMN+1)', TAMN1, 'porcentaje', 'anual', 'SBS'],
    [fecha_consulta_f, 'Moneda Nacional (TAMN+2)', TAMN2, 'porcentaje', 'anual', 'SBS'],
    [fecha_consulta_f, 'Moneda Extranjera (TAMEX)', TAMEX, 'porcentaje', 'anual', 'SBS'],
]
df = pd.DataFrame(data, columns=['fecha_consulta', 'tipo_interes', 'valor', 'unidad', 'frecuencia', 'fuente'])

# Guardar CSV
nombre_archivo = f"tasas_{fecha_consulta_f}.csv"
df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
print("Archivo " + nombre_archivo + " generado correctamente.")
