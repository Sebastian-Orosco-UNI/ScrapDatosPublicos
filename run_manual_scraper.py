import os
from datetime import datetime, timedelta

start = datetime.strptime(os.environ['FECHA_INICIO'], '%d/%m/%Y')
end = datetime.strptime(os.environ['FECHA_FIN'], '%d/%m/%Y')
current = start

while current <= end:
    fecha = current.strftime('%d/%m/%Y')
    print(f'Procesando: {fecha}')
    os.environ['FECHA_CONSULTA'] = fecha
    os.system('python scrapersbs.py')
    current += timedelta(days=1)
