segundos = int(input("Informe a quantidade de segundos: "))

dias = segundos // 86400
resto_dias = segundos % 86400
horas = resto_dias // 3600
minutos = (resto_dias % 3600) // 60
segundos_restantes = (resto_dias % 3600) % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos_restantes, "segundos.")