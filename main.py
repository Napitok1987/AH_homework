import csv

name = input('Enter your name: ')
email = input('Enter your email: ')
phone = input('Enter your phone number: ')
Git_profile = input('Enter link to your Git profile: ')
save = input('Save to CSV? ')
if save == 'yes' or "y":
    file = open('results.csv', 'a')
    csv_writer = csv.writer(file)
    csv_writer.writerow([name, email, phone, Git_profile])
