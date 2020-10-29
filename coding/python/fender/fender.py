import csv

compromised_users = []

with open('passwords.csv', newline='', encoding='utf-8-sig') as password_file:
    password_csv = csv.DictReader(password_file)
    #open up the csv files to make sure that the contents are not enclosed with quotations, then you will not be able to access the keys.
    #OUTPUT DOES NOT CHANGE WHEN RUNNING ROWS WITHOUT TRYING TO ONLY ACCESS A CERTAIN KEY, so must open up file
    for row in password_csv:
        compromised_users.append(row['Username'])
