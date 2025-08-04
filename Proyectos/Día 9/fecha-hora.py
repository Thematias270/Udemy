# from datetime import datetime
# from datetime import date
# import datetime

# mi_hora = datetime.time(17, 35)

# print(mi_hora)
# print(mi_hora.hour)

# mi_dia = datetime.date(2025, 10, 17)
# print(mi_dia)
# print(mi_dia.ctime())
# print(mi_dia.today())

# mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)

# mi_fecha = mi_fecha.replace(month=11)

# print(mi_fecha)

# nacimiento = date(1995, 3, 5)
# defuncion = date(2095, 6, 19)

# vida = defuncion - nacimiento

# print(vida.days)

# despierta = datetime(2022, 10, 5, 7, 30)
# duerme = datetime(2022, 10, 5, 23, 45)

# vigilia = duerme - despierta

# print(vigilia.seconds)

from datetime import datetime

minutos = datetime.now().minute

print(minutos)
