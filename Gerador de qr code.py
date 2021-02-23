from pyqrcode import QRCode
from cryptography.fernet import Fernet
import cv2
import mysql.connector
from mysql.connector import errorcode


#diretorio do banco de dados;
def inputBD(Nick,Keygen,hashgen,data,empresa):
    "Fazer Conexão com o Banco de dados"
    cnx = mysql.connector.connect(user='user', password='password',host='localhost',database='hashsave')
    cursor=cnx.cursor()
    "inserir tag, Hash, key, empresa no Banco de dados"
    data_employee = (f'{Nick}',f'{Keygen}',f'{hashgen}',f'{data}',f'{empresa}')
    add_info=("INSERT INTO instagram_code" "(NICKNAME, keygen, hashgen, timepost, EMPRESA) " "VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(add_info,data_employee)
    cnx.commit()
    return

def outputBD():
    "Fazer Conexão com o Banco de dados"
    cnx = mysql.connector.connect(user='user', password='password',host='localhost',database='hashsave')
    cursor = cnx.cursor()
    "Consultar o banco de dados"
    oasi = ("select NICKNAME, keygen, hashgen, timepost, EMPRESA from instagram_code")
    cursor.execute(oasi)


#gerador e leitor de qr code:
class QrcodeRG:

    'Gerador de QrCode'
    def Generator(self,data):
        self.data=data
        img=QRCode(data)
        g=fr'{data}.png'
        img.png(fr"C:\Users\marqu\Documents\DOCUMENTOS MARK\Programas\PYTHON\SISTEMA DE DESCONTO\banco de dados\{g}", scale=5)

    "Leitor de QrCode"
    def Reader(self,filename):
        self.filename=filename
        img=fr"C:\Users\marqu\Documents\DOCUMENTOS MARK\Programas\PYTHON\SISTEMA DE DESCONTO\banco de dados\{filename}"
        detector=cv2.QRCodeDetector()
        x=cv2.imread(img)
        f=detector.detectAndDecode(x)
        return print(f[0])

#Código para fazer uma hash and Key com: desconto, nickname, informações complementares, nome da empresa. Para geração de qr code;
class HashGenerator:
    "Criptografar"
    def encrypt(self,valores):
        self.valores=valores
        key=Fernet.generate_key()
        f=Fernet(key)
        g=valores.encode()
        tokenG = f.encrypt(g)
        return tokenG,key

    "Descriptografar"
    def decrypt(self,tokenG,Key):
        self.tokenG=tokenG
        self.Key=Key
        key=Key
        f=Fernet(key)
        dec=f.decrypt(tokenG)
        return dec

