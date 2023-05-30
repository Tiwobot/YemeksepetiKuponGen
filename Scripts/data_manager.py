import pickle

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