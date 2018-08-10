from Email import Email
from ServiceDeskAPI import ServiceDeskAPI

#email = Email("pythontestemeli@gmail.com","Meli1234")
#email.sendEmaiil("leonardo.dylan@mercadolivre.com","teste","teste")

ticket = ServiceDeskAPI(420)
print(ticket._mesa)