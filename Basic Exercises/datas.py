from datetime import datetime, timedelta

data_atual = datetime.now()
data_futura = data_atual + timedelta(2)

data_futura_formatada = data_futura.strftime('%d/%m/%Y  %H:%M:%S')

print(data_futura_formatada)