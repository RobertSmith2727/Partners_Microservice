'''sequence
call sendToMicro() sends form data to the MicroReceiveChan.py
Form data must be a list of strings
This sends the form data to the channel listening and calls sql.py
this creates a SQL statement from the form data and calls sendToPartner()
which sends that statement to PartnerReceiveChan.py which my partner
will handle the SQL statment'''

from sender import sendToMicroservice

a = ["Robert", "Smith", "Words about me", "123@gmail.com", "pass123", "Tutor"]

sendToMicroservice(a)

# body = b'["Ro bert", "Smith", "Words about me", "123@gmail.com", "pass123",
# "Tutor"]'
# data = []
# string = ''
# newBody = body.decode('ascii')

# for element in newBody:
#     if element == '[' or element == '"' or element == "'":
#         element = ''
#     if element == ' ' and newBody[newBody.index(element) + 1].isalpha():
#         string = string + element
#     elif element == ',' or element == ']':
#         data.append(string)
#         string = ''
#     else:
#         string = string + element


# # for element in newBody:
# #     if element == '[' or element == '"' or element == "'" or element
# == ' ':
# #         pass
# #     elif element == ',' or element == ']':
# #         data.append(string)
# #         string = ''
# #     else:
# #         string = string + element
# print(data)
