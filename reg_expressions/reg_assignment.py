import re


def check_date_format(date):
    #MM/DD/YYYY
    list = ''
    match_year = re.findall(r'([0-1]|[0-9]{2})/([0-3]|[0-9]{2})/([0-9]{4})', date)
    for match in match_year:
        match = '/'.join(match)
        list = list + ' ' + match
    return list

def check_email_format(email):
    #user@email.com
    list = ''
    match_email = re.findall(r'[\w\.-]+@[\w\.-]+', email)
    for match in match_email:
        list = list + ' ' + match
    return list
    
def check_phone_format(phone):
    # (XXX) XXX-XXXX
    list = ''
    match_phone = re.findall(r'\(\d{3}\) \d{3}-\d{4}', phone)
    for match in match_phone:
        list = list + ' ' + match
    return list

def check_website_format(website):
    #http(s)://www.domain.com/path/to/page.html", where "(s)" is optional and indicates that the connection should be secure, "www" is optional and can be replaced by any subdomain, "domain.com" can be any valid domain name, and "/path/to/page.html" can be any path or file name.
    list = ''
    match_website = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', website)
    for match in match_website:
        list = list + ' ' + match
    return list

def check_string_format(string):
    # string that contains at least one uppercase letter, one lowercase letter, and one digit, and is between 8 and 20 characters long
    list = ''
    match_string = re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*?[0-9]).{8,20}', string)
    for match in match_string:
        list = list + ' ' + match
    return list

def check_string2_format(string):
    #string that contains only letters, numbers, and spaces, and is between 5 and 50 characters long.
    list = ''
    match_string2 = re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)([\s]).{5,50}', string)
    for match in match_string2:
        list = list + ' ' + match
    return list

def check_string3_format(string):
    #string that contains at least one uppercase letter, one lowercase letter, one digit, and one special character, and is between 8 and 20 characters long.
    list = ''
    match_string3 = re.findall(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$', string)
    for match in match_string3:
        list = list + ' ' + match
    return list

def check_card_format(card):
    # XXXX-XXXX-XXXX-XXXX
    list = ''
    match_card = re.findall(r'\d{4}-\d{4}-\d{4}-\d{4}', card)
    for match in match_card:
        list = list + ' ' + match
    return list



if __name__ == '__main__':

    date = "02/27/2019, 12/15/2019, 12-16-2019, 12.17.2019, 30/30/9999"
    email = 'user99@google.com, 1useR@hotmail.com, user_11@yahoomail.com'
    website = 'http://www.google.com, https://www.yahoo.com, http://www.google.com/path/to/page.html, https://www.yahoo.com/path/to/page.html'
    phone = '(123) 456-7890, 123-456-7890, 123.456.7890'
    string = 'password9, Password123, password 123, Password123!'
    string2 = 'password 123'
    card = '1234-5678-9012-3456, 9876-5432-1000-0000, 1234/1234/1234/1234, 1234.1234.1234.1234, 1234 4568 9012 3456'
    print('1. ', check_date_format(date))
    print('2. ', check_email_format(email))
    print('3. ', check_website_format(website))
    print('4. ', check_phone_format(phone))
    print('5. ', check_string_format(string))
    print('6. ', check_string2_format(string))
    print('7. ', check_string3_format(string))
    print('8. ', check_card_format(card))