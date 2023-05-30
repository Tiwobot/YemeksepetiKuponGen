import pickle


def save_mail(mail):
    try:
        with open("mail.data", "wb") as f:
            pickle.dump(mail, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during saving mail:", ex)

def load_mail():
    try:
        with open("mail.data", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)