import encode
import os 
import decode
encrypt = encode.Encode()
decrypt = decode.Decode()
def f1():
  plain_text = input("Enter text for encoding: ")
  security_key = int(input("Enter your security key: "))
  if security_key  < 26 :
  
      
    encrypt.update_on_list(plain_text,security_key)
  else:
    print("Please enter the security less than 26 ! ")

  encrypt.encode()
  print(f"Your encoded text is : {encrypt.encoded_text}")

#decryption
def f2 ():
    
    

    encoded_text = input("Enter text for decoding: ")
    security_key = int(input("Enter your security key: "))
   
    
    decrypt.decode(encoded_text,security_key)
    print(f"your decrypted text is : {decrypt.decoded_text}")
operation =True 
while operation:
   select_mode  = int(input('Select operations : \n1.encrypt\n2.decrypt\n'))
   
   if select_mode == 1:
      f1()
   elif select_mode == 2:
      f2()
   else :
      print("please select valid option")
    
