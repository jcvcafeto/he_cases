import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

from functions import remove_repetitive_elements

class Ticket(object):
    def __init__(
        self,summary,issue_key,issue_id,
        issue_type, status, project_lead, priority,
        resolution, assignee, created, updated,
        last_view, resolved, labels
    ):
        self.summary = summary
        self.issue_key = issue_key
        self.issue_id = issue_id
        self.issue_type = issue_type
        self.status = status
        self.project_lead = project_lead
        self.priority = priority
        self.resolution = resolution
        self.assignee = assignee
        self.created = created
        self.updated = updated
        self.last_view = last_view
        self.resolved = resolved
        self.labels = labels

    
    @staticmethod
    def convert_all_tickets(data):
        """
        Takes a panda DataFrame and returns an array of Ticket
        object type.
        """
        count = 0
        total_rows = len(data)
        tickets = []

        while total_rows > count:
            # Etiquetas
            labels = [
                data.at[count,'Labels'],
                data.at[count,'Labels.1'],
                data.at[count,'Labels.2'],
                data.at[count,'Labels.3'],
                data.at[count,'Labels.4'],
                data.at[count,'Labels.5'],
                data.at[count,'Labels.6'],
                data.at[count,'Labels.7']
            ]
            # Remover elementos repetitivos de la lista de etiquetas
            labels = remove_repetitive_elements(labels)
            # Creacion de objetos Ticket
            ticket = Ticket(
                data.at[count,'Summary'], data.at[count,'Issue key'], data.at[count,'Issue id'],
                data.at[count,'Issue Type'], data.at[count,'Status'], data.at[count,'Project type'],
                data.at[count,'Priority'], data.at[count,'Resolution'], data.at[count,'Assignee'],
                data.at[count,'Created'], data.at[count,'Updated'], data.at[count,'Last Viewed'],
                data.at[count,'Resolved'], labels
            )
            # Lista de objetos tipo tickets
            tickets.append(ticket)
            count = count + 1
        
        return tickets


    @staticmethod
    def get_priority_tickets(tickets):
        """
        Return the quantity of tickets according with its priority.
        """
        low_qty = 0
        medium_qty = 0
        high_qty = 0
        urgent_qty = 0

        for ticket in tickets:
            if ticket.priority == "Low":
                low_qty += 1
            elif ticket.priority == "Medium":
                medium_qty += 1
            elif ticket.priority == "High":
                high_qty += 1
            elif ticket.priority == "Urgent":
                urgent_qty += 1

        print('Tickets con prioridad baja: {}'.format(low_qty))
        print('Tickets con prioridad media: {}'.format(medium_qty))
        print('Tickets con prioridad alta: {}'.format(high_qty))
        print('Tickets con prioridad urgente: {}'.format(urgent_qty))

        return [low_qty,medium_qty,high_qty,urgent_qty]


    @staticmethod
    def get_escalated_tickets(data):
        """
        Receives a panda DataFrame and returns a DataFrame with the escalated tickets.
        """
        # Filtrar tickets por Status == Escalated
        escalated_tickets = data.loc[data['Status'] == 'Escalated']
        # Total de tickets escalado
        escalated_qty = len(escalated_tickets)
        print("Escalated Tickets: {0}".format(escalated_qty))
        return escalated_tickets

        

