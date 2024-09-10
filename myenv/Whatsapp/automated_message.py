import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Ludo Chamar", 21, 55)