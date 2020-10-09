# Name:         Rusif Eyvazli
# Company:      ASYMMETRIK
# Challenge:    Business Card OCR
# Purpose:      The program takes the business card text as an input and outputs the 
#               Name, Phone, and Email Address of the owner of the business card.

import sys
import re

# if exists, takes the example file as an argument. Otherwise returns an error
try:
    data_file = sys.argv[1] 
except IndexError:
    print("Usage: ocr.py", "<data_file>\n")
    sys.exit(1)

# ContactInfo class holds the constructor and the getters 
class ContactInfo:

    def __init__(self, name=None, number=None, email=None):
        self.m_name = name
        self.m_number = number
        self.m_email = email

    def getEmailAddress(self):  # returns the email address
        return self.m_email
    
    def getPhoneNumber(self):   # returns the phone number formatted as a sequence of digits
        return self.m_number

    def getName(self):      # returns the full name of the individual (eg. John Smith, Susan Malick)
        return self.m_name

# BusinessCardParser class holds the functions
class BusinessCardParser:

    # getContactInfo function accepts the data document as an argument. If the file 
    # does not exist, an error message is printed out. Otherwise, for each line, 
    # email, phone, name is being processed and returned as a ContactInfo object.
    def getContactInfo(self, document):
        try:
            data_file = open(document, 'r')
        except IOError:
            print('Error: File does not exist. Please try again! \n')
            exit()
        
        # Initializes the variables and sets them to None
        _name = None
        _email = None
        _phone = None

        lines_list = data_file.readlines()          # returns a list with lines being list items
        data_file.close()                           # closes the data file
        lines =[e.strip() for e in lines_list]      # returns a copy of the lines with \n removed from the end
        
        # Loops through the lines of the file and processes the email and the phone number if the condition is set to None
        for line in lines:
            if _email == None:
                _email = self.processEmail(line)
            
            if _phone == None:
                _phone = self.processPhone(line)
                
        if _name == None:
            _name = self.processName(lines, _email)

        info = ContactInfo(_name, _phone, _email)   # assigns ContactInfo object to info variable
        return info
        # end of getContactInfo()
# end of BusinessCardParser class

    # Processes the email using regex (re) library. If found, assigns it to info_email. 
    # Otherwise appears as "None", its initial condition.
    def processEmail(self, email):
        reg_exp = re.compile('[^@]+@[^@]+\.[^@]+')
        info_email = re.search(reg_exp, email)
        if info_email != None:
            return info_email.group()
    # end of processEmail()

    # Processes the phone number using regex (re) library. First, find the first element in the line.
    # Then, checks if it is Fax; If so, returns None, otherwise, if found, assigns it to phone 
    # after correcting the output style.
    def processPhone(self, number):
        ph = number.split(' ')[0].lower()   # first element of each line
        if ph != "fax:":
            reg_exp = re.compile('(1)?\s?\(?(\d{3})\D{0,3}(\d{3})\D{0,3}(\d{4})')
            info_phone = re.search(reg_exp, number) # searches for the regex styled text
            if info_phone != None:
                replacements = {            # replacing the parenthesis, dash, +, and space with non-space.
                    "(" : '',
                    ")" : '',
                    "-" : '',
                    "+" : '',
                    " " : ''
                }
                phone = "".join([replacements.get(c, c) for c in info_phone.group()])   # joins all the digits in the group
                return phone
    # end of processPhone()

    # Processes and returns the name. First, while going through 'for-loop', groups first and seconds elements under
    # first and last names accordingly. Then, checks if either first or last name is a part of the email. If so,
    # returns the name. Otherwise, returns None  
    def processName(self, data_lines, email):
        for idx in data_lines:
            info_name = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", idx)
            if info_name and email is not None:
                fn = info_name.group('first_name')
                ln = info_name.group('last_name')
                # print ("info_name: ", fn, ln)
                em=email.split('@')[0].lower()              # takes the first part of the email (before @) in lowercase
                if fn.lower() in em or ln.lower() in em:    # checks if first or last name is in the first of the email
                    return info_name.group()
    # end of processName()
# end of ContactInfo class 

# Main function
def main():
    # Function object of BusinessCardParser class with data_file as an argument assigned to OCR
    OCR = BusinessCardParser().getContactInfo(data_file)

    # Print statements to print out the 'grabbed' information
    print("Email: ", OCR.getEmailAddress())
    print("Phone: ", OCR.getPhoneNumber())
    print("\nName:  ", OCR.getName(), "\n")


# end of main()    

#Calling main function
main()