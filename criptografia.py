import time
import getpass, sys
import pyAesCrypt
from os import stat, remove


bufferSize = 64 * 1024

escolha = input('digite: \n1- encriptar \n2- descriptografar1\nR: ')


password = getpass.getpass('\nDigite a Senha:')

if escolha == '1':
 # encripita
 with open("ss.txt", "rb") as fIn:
  with open("ss.txt.aes", "wb") as fOut:
   pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

 x = input ('deletar arquivo original? s ')

 if x != 's':
  print ('\nok')
  time.sleep(1)
  sys.exit()
  
 remove("ss.txt")
 print ('Arquivo removido')
 time.sleep(2)
 sys.exit()

if escolha == '2':
 
 encFileSize = stat("ss.txt.aes").st_size

 # remove encriptação
 with open("ss.txt.aes", "rb") as fIn:
  try:
   with open("ss.txt", "wb") as fOut:
 
    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
  except ValueError:
   print ('senha incorreta')
   # remove arquivo
   remove("ss.txt")

 time.sleep(3)
 sys.exit()

print ('\n\nEscolha errada')
time.sleep(2)