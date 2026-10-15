# AI master class week 2 project
# lists and dictionaries
# contack book practice

contacts = [
    {"name": "Wycliff Nganga", "phone_number": "0740885259", "city": "Nairobi", "skill": "Human Resource Professional"},
    {"name": "Lawrence Thuo", "phone_number": "0701028515", "city": "Nyeri", "skill": "Mechanical engineer"},
    {"name": "Edith Njoki", "phone_number": "0726775796", "city": "Nairobi", "skill": "Farmer"},
    {"name": "Julius Nganga", "phone_number": "0722911611", "city": "Meru", "skill": "Electrician"},
    {"name": "Hunk Mudy", "phone_number": "0748569525", "city": "New york", "skill": "Actor"},
    {"name": "Travis Green", "phone_number": "0152545898", "city": "Nairobi", "skill": "singer"}
]

print("\n===== CONTACT BOOK =====")
print(f"contacts found: ", len(contacts))
# for i, contact in enumerate(contacts):
#     print(f"\n{i+1}. {contact['name']}")
#     print(f"   Phone : {contact['phone_number']}")
#     print(f"   Skill : {contact['skill']}")
#     print(f"   City  : {contact['city']}")

# search for several names
# search_name = input("input a name to see if its there?")
# found = False

# for contact in contacts:
#     if contact["name"] == search_name:
#         print("Contact found:")
#         print(f"  Name  : {contact['name']}")
#         print(f"  Phone : {contact['phone_number']}")
#         print(f"  Skill : {contact['skill']}")
#         print(f"  City  : {contact['city']}")
#         found = True
#         break

# if not found:
#     print("No contact found with name:", search_name)

#     #search with city
# search_city = "Nairobi"
# print(f"Contacts in {search_city}:")

# for contact in contacts:
#     if contact["city"] == search_city:
#         print(f"  {contact['name']} | {contact['skill']} | {contact['phone_number']}")
new_contact = {"name": "James Mbaru", "phone_number": "0478855259", "city": "Kaimbu", "skill": "athlete"}
contacts.append(new_contact)
print("Last contact:", contacts[-1])