"""
1. Diferenciar todas las etiquetas
2. Hallar etiquetas más repetitivas
3. Diferenciar tiquetes escalados en Frontend y Backend
"""


import pandas as pd
import math

from ticket import Ticket


# Importar CSV files
data = pd.read_csv('jira_cases.csv')

# Total de datos
total_rows = len(data)
print("Total rows: {0}".format(total_rows))

#Convierte el DataFrame a una lista de objetos tipo Ticket
tickets = Ticket.convert_all_tickets(data)
print(len(tickets))

# Prioridades de los tickets
lowp, mediump, highp, urgentp = Ticket.get_priority_tickets(tickets)

# Obtiene el total de tickets escalados en DataFrame
escalated_tickets = Ticket.get_escalated_tickets(data)
print(escalated_tickets.iloc[0]['Created'])

"""
# Numero de tiquets escalados Frontend
frons = 0
for ticket in tickets:
    if 'Frontend' in ticket.labels:
        frons += 1
print('Tickets Frontend: {0}'.format(frons))

# Numero de tiquets escalados Backend
backs = 0
for ticket in tickets:
    if 'Backend' in ticket.labels:
        backs += 1
print('Tickets Backend: {0}'.format(backs))

# Numero de tiquets escalados Monetization
monets = 0
for ticket in tickets:
    if 'Monetization' in ticket.labels:
        monets += 1
print('Tickets Monetization: {0}'.format(monets))

# Tickets sin etiqueta de diferenciacion
fbm = frons + backs + monets
print('Tickets sin Nomenclatura: {0}'.format(escalated_rows - fbm))
"""