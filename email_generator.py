import requests
import random
import string
import xlsxwriter


email = ''
password = ''
e_list = []
p_list = []
amount = ''
file_name = ''


def inputs():
    global file_name
    global amount
    file_name = input('What would you like to call the file? ')
    amount = int(input('How many emails would you like to generate? '))


def random_email(chars=str('...............')+string.ascii_letters + string.digits):
    email = str(random.choice(string.ascii_letters) + (''.join(random.choice(chars) for i in range(0, random.randint(5, 15)))) + random.choice(string.ascii_letters) + '@gmail.com')
    print('Email: ' + email)
    e_list.append(email)


def random_passwords(chars=string.ascii_letters + string.digits + string.punctuation):
    password = str(''.join(random.choice(chars)for i in range(0, random.randint(8, 15))))
    print('Password: ' + password)
    p_list.append(password)


def email_and_password():
    random_email()
    random_passwords()


def xlsx():
    global password
    global email
    workbook = xlsxwriter.Workbook(f'{file_name}.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 50)
    worksheet.set_column('B:B', 50)
    row = 0
    col = 0
    worksheet.write(row, col, 'Emails:')
    worksheet.write(row, col + 1, 'Passwords:')
    for row_num, data in enumerate(e_list):
        worksheet.write(row_num+1, 0, data)
    for row_num, data in enumerate(p_list):
        worksheet.write(row_num+1, 1, data)
    workbook.close()


inputs()
for i in range(0, amount):
    email_and_password()
xlsx()