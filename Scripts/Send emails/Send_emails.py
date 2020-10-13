#####################################################################
#        This script will send personalized emails                  #
#####################################################################

import csv, smtplib, config

# Create message
message = """Subject: Your grade

Hi {name}, your grade is {grade}"""

# Import email address and password from config
from_address = config.My_email
password = config.My_pass

# Create connection
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.connect("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(from_address, password)
    # Open csv file 
    with open("test.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            smtp.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )
    print("Emails sent.")

         