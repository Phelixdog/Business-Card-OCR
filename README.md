# Business-Card-OCR
The program takes the business card text as an input and outputs the name, phone, and email address of the business card owner.

# Details
The sample input files, *example1.txt, example2.txt, example3.txt* have been provided included person's name, title, company's name, address, telephone number, fax number, and email. In some sample input files, one or more of this information was not provided. The program first calls the main function, which then prints the name, phone number, and email address information of the business cardholder. 

To print the email address, first, the processEmail function uses regular expressions against the email format. Once found the matching format, it returns it; otherwise, the result prints as None as an initial condition.

To print the phone number, the first elements of the lines in the data were found. Then, an if statement checks if the found piece is Fax; If so, the program returns None as an initial condition; otherwise, if the first element is the phone number, the program first replaces all the symbols with non-space and then assigns the 10-11 digits to the phone variable.  

To print the name, the function processName takes the lines of the data and email as arguments. Within the loop that goes through all the data lines, the first two elements are matched and grouped under first and last names using regex's .match method. Then the first part of the email, the part before the '@' sign is picked and turned into lowercase. Then, each element in the lines was checked against the part of the email. If the element is part of the email, the program accepts it as the Card Owner's name. Otherwise, it may be the company's name, address, or other information that may be provided. Using this method applies only the cases if the person's name, either first or last, is in their email address. In the given examples, this method applied to all of them since the condition above met for all. Besides, thinking that business owners are most likely to have their names in their emails, this method would work most of the time.

# How To Run
1. Download the zip file of the repository and extract the files;
2. Open your command line and change the directory to the folder that the files were extracted into;
3. Run the program using python command with one argument; that is the data file. For example:

    
    ```py ocr.py example1.txt```
    
    OR
    
    ```python ocr.py example2.txt```

# NOTE:
## Tested Environment
This program was tested on Microsoft Windows 10 Home OS using Python 3.8.5.

## Used Libraries
The following two libraries were used in the process of making and running the program:

* sys
* re

