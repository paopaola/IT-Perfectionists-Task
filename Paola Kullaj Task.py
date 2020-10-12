import json

# Declaration of class Contacts
class Contacts:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


# Append objects from class Contacts to ContactsList
ContactsList = []
ContactsList.append(Contacts('Alice Brown', '', '1231112223'))
ContactsList.append(Contacts('Bob Crown', 'bob@crowns.com', ''))
ContactsList.append(Contacts('Carlos Drew', 'carl@drewess.com', '3453334445'))
ContactsList.append(Contacts('Doug Emerty', '', '4564445556'))
ContactsList.append(Contacts('Egan Fair', 'eg@fairness.com', '5675556667'))

# Declaration of class Leads
class Leads:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


# Append objects from class Leads to LeadsList
LeadsList = []
LeadsList.append(Leads('', 'kevin@keith.com', ''))
LeadsList.append(Leads('Lucy', 'lucy@liu.com', '3210001112'))
LeadsList.append(Leads('Mary Middle', 'mary@middle.com', '3331112223'))
LeadsList.append(Leads('', '', '4442223334'))
LeadsList.append(Leads('', 'ole@olson.com', ''))

# JSON data from registrants
registrant1 = '{"name": "Lucy Liu", "email": "lucy@liu.com", "phone": ""}'
registrant2 = '{"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"}'
registrant3 = '{"name": "Uma Thurman", "email": "uma@thurs.com", "phone": ""}'

# Convert from JSON to Python and add dictionaries to RegistrantsList
RegistrantsList = []
RegistrantsList.append(json.loads(registrant1))
RegistrantsList.append(json.loads(registrant2))
RegistrantsList.append(json.loads(registrant3))

# Match registrant's email to Contacts List.
# If not matched, match registrant's phone to Contacts List
# Update the missing info (email/phone) at Contacts List
del_reg_index = []  #list of indexes of registrants that match with any contacts
for reg in RegistrantsList:
    for contact in ContactsList:
        if reg["email"] and reg["email"] == contact.email:
            del_reg_index.append(RegistrantsList.index(reg))
            if not contact.phone:
                contact.phone = reg["phone"]
            break
        elif reg["phone"] and reg["phone"] == contact.phone:
            del_reg_index.append(RegistrantsList.index(reg))
            if not contact.email:
                contact.email = reg["email"]
            break

# delete the matched registrants from the RegistrantsList
for index in sorted(del_reg_index, reverse=True):
    del RegistrantsList[index]

# Match registrant's email to Leads List.
# If not matched, match registrant's phone to Leads List.
# Update the missing info (name/email/phone) at Contacts List.
# Add matched registrants to Contacts List.
del_reg_index = []  #list of indexes of registrants that match with any contacts
del_lead_index = []  #list of indexes of leads that are added to contacts
for reg in RegistrantsList:
    for lead in LeadsList:
        if reg["email"] and reg["email"] == lead.email:
            del_reg_index.append(RegistrantsList.index(reg))
            del_lead_index.append(LeadsList.index(lead))
            if not lead.phone:
                lead.phone = reg["phone"]
            if not lead.name:
                lead.name = reg["name"]
            ContactsList.append(Contacts(lead.name, lead.email, lead.phone))
            break
        elif reg["phone"] and reg["phone"] == lead.phone:
            del_reg_index.append(RegistrantsList.index(reg))
            del_lead_index.append(LeadsList.index(lead))
            if not lead.email:
                lead.email = reg["email"]
            if not lead.name:
                lead.name = reg["name"]
            ContactsList.append(Contacts(lead.name, lead.email, lead.phone))
            break

# delete the matched registrants from the RegistrantsList
for index in sorted(del_reg_index, reverse=True):
    del RegistrantsList[index]

# delete leads that are already appended to ContactsList
for index in sorted(del_lead_index, reverse=True):
    del LeadsList[index]

# If not matched, simply add it to ContactsList
for reg in RegistrantsList:
    ContactsList.append(Contacts(reg["name"], reg["email"], reg["phone"]))

# print contacts list
print("Contacts List:")
for contact in ContactsList:
    print(contact.name, contact.email, contact.phone, sep=' - ')

