import imaplib, email 
from email.header import decode_header, make_header  
import os 
from colorama import Fore, Back, Style 

os.system("cls")

host = 'imap.gmail.com' 
username = "solis.krlos@gmail.com" 
password = "jcspperu"

sw = 0
try:
    mail = imaplib.IMAP4_SSL(host) 
    mail.login(username, password) 
    sw = 1 
except:
    sw = 0
    print("An exception occurred")


def leer():
    #lista de carpetas
    #print(mail.list()) 
    
    # unseen = sin ver 
    # all  
    _ , search_data  = mail.search('UTF8', "(unseen)") 

    con = 0
    for msgnum in search_data[0].split(): 
        _, data = mail.fetch(msgnum, "(RFC822)")
        
        message = email.message_from_bytes(data[0][1]) 

        # print(f"message number: {msgnum}")
        con+=1  
        print(Fore.LIGHTYELLOW_EX, f"{con})")
        print(Fore.CYAN, "Desde : ", end = " ")
        print(Fore.WHITE, message.get('From')) 
        print(Fore.GREEN, "Asunto: ", end = " ")
        h = make_header(decode_header(message.get('Subject')))
        print(str(h)) 
        print(Style.RESET_ALL) 

        # evita poner mensaje como leido
        mail.store(msgnum, '-FLAGS', '(\SEEN)') 


if sw == 1:
    print("/************ RECIBIDOS ************/")
    _, mensajesinbox = mail.select("inbox") 
    leer()
    print("/************ SPAM ************/")
    _, mensajesspam = mail.select("[Gmail]/Spam") 
    leer()

    mail.close()
    mail.logout()
