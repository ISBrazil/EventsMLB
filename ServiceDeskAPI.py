import requests
import sys

class ServiceDeskAPI(object):

    def __init__(self, mesa):
        self._mesa = mesa
        #self._url = 'https://mercadolibre:GPxK6FEnMWflkw6ik22pevuy@servicedesk.mercadolibre.com/api'
        self._url = 'https://is-support:S9xV2l7IUOVFgVRaIRCo60KO@servicedesk.mercadolibre.com/api'

    def unescapeString(self, txt):
        p = txt.replace("<br />", "")
        p = p.replace("<p>", "")
        p = p.replace("</p>", "")
        p = p.replace("p&gt;", "")
        p = p.replace("/&gt;", "")
        p = p.replace("/&gt;", "")
        p = p.replace("<em>", "")
        p = p.replace("</em>", "")

        return p

    def getOpen_Tickets_Mesa(self):
        httpAPI = '/v1/incidents.by.helpdesk'
        payload = {'helpdesk_id': self._mesa}
        try:
            open = requests.get(self._url + httpAPI, params=payload)
            response = open.json()
            tickets = response['requestIds']
        except OSError as err:
            tickets = "OS error: {0}".format(err)
        except ValueError:
            tickets = "Could not close data to an integer."
        except:
            tickets = "Unexpected error:", sys.exc_info()[0]

        return tickets


    def getIncidentCategory_Ticket_Information(self, tickets, category):
        #httpAPI = 'https://mercadolibre:GPxK6FEnMWflkw6ik22pevuy@servicedesk.mercadolibre.com/api/v1/incident?id='
        httpAPI = 'https://is-support:S9xV2l7IUOVFgVRaIRCo60KO@servicedesk.mercadolibre.com/api/v1/incident?id='

        informationTickets = []
        informationTicket = []
        #tickets = {471641}
        for ticket in tickets:
            response = requests.get(httpAPI + str(ticket))
            response = response.json()
            if category == response['category_id']:
                information = response['description']
                information = self.unescapeString(information)

                informationTicket.append(ticket)
                informationTicket.append(information)
                informationTickets.append(informationTicket)
                informationTicket = []

        return informationTickets

    def putReassign_Agent(self, ticket, mesa, author_Closer):
        httpAPI = '/v1/incident.reassign'
        payload = {'request_id': ticket, 'group_id': mesa, 'author_id': 2,  'agent_id': author_Closer}  # cierre
        try:
            r = requests.post(self._url + httpAPI, params=payload)
            return r
        except OSError as err:
            return "OS error: {0}".format(err)
        except ValueError:
            return "Could not close data to an integer."
        except:
            return "Unexpected error:", sys.exc_info()[0]

    def putReassign_Mesa(self, ticket, mesa):
        httpAPI = '/v1/incident.reassign'
        payload = {'request_id': ticket, 'group_id': mesa, 'author_id': 2}  # cierre
        try:
            r = requests.post(self._url + httpAPI, params=payload)
            return r
        except OSError as err:
            return "OS error: {0}".format(err)
        except ValueError:
            return "Could not close data to an integer."
        except:
            return "Unexpected error:", sys.exc_info()[0]

    def putClose_Ticket(self, ticket, comment, author_Closer):
        httpAPI = '/v1/incident.comment'
        solution = True
        payload = {'comment': comment, 'request_id': ticket, 'author_id': author_Closer, 'is_solution': solution} #cierre
        try:
            r = requests.post(self._url+httpAPI, params=payload)
            return r
        except OSError as err:
            return "OS error: {0}".format(err)
        except ValueError:
            return "Could not close data to an integer."
        except:
            return "Unexpected error:", sys.exc_info()[0]