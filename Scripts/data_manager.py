from datetime import timedelta
from datetime import datetime
import pickle
import random
import secrets
import string

first_names=('Akman','Cengiz','Cenk','Berke','Selin','Sevda','Berkcan','Zişan','Eren','Numan','Yuşa','Ceren','Çağla','Salih','Ahmet','Bora','Giray','Gül','Haşmet','Yurtseven','Zeynep','Defne','Elif', 'Asya', 'Azra', 'Nehir', 'Eylül', 'Göktuğ', 'Ömer Asaf', 'Eymen', 'Aras','Merve', 'Kübra', 'Cankut', 'Caner', 'Barın', 'Ekin', 'Edis', 'Haluk')
last_names=('Sevinç','Ağaoğlu','Demir','Yıldırım','Yılmaz','Abalıoğlu','Damar','Korkmaz','Yaman','Yavuz','Devran','Devrim','Emre','Tunç','Açıkgöz','Bademci','Kaya','Çelik', 'Şahin', 'Yıldız', 'Öztürk', 'Aydın', 'Özdemir', 'Arslan', 'Aslan', 'Doğan', 'Kılıç', 'Çetin', 'Kara', 'Koç', 'Kurt')
symbols = ['*', '%', '£', '.', '?']

def set_mailAddress(mail):
    try:
        with open("mail.data", "wb") as f:
            pickle.dump(mail, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during saving mail:", ex)

def set_mail_authLink(link):
    try:
        with open("AuthLink.data", "wb") as f:
            pickle.dump(link, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during saving authlink:", ex)

def get_mailAddress():
    try:
        with open("mail.data", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during loading mail:", ex)

def get_mailLink():
    try:
        with open("mail.data", "rb") as f:
            return "https://generator.email/"+pickle.load(f)
    except Exception as ex:
        print("Error during loading link:", ex)

def get_mail_authLink():
    try:
        with open("AuthLink.data", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during loading authlink:", ex)

def random_firstName():
    return random.choice(first_names)

def random_lastName():
    return random.choice(last_names)

def random_date():
    start = datetime.strptime('1/1/1980', '%m/%d/%Y')
    end = datetime.strptime('1/1/2004', '%m/%d/%Y')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return((start + timedelta(seconds=random_second)).strftime("%m%d%Y"))

def random_password():
    password = ""
    for _ in range(9):
        password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.digits)
    try:
        with open("password.data", "wb") as f:
            pickle.dump(password, f, protocol=pickle.HIGHEST_PROTOCOL)
            return password
    except Exception as ex:
        print("Error during saving password:", ex)

def get_lastPassword():
    try:
        with open("password.data", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during loading password:", ex)