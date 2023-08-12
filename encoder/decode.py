
class Decode ():
    def __init__(self):
         self.alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
         self.key = 0
         self.new_index = [] 
         self.decoded_text = ""
    def decode(self,encoded_text,security_key):
         self.key +=security_key
         
         for _ in encoded_text:
              new =self.alphabets.index(_)-self.key
              self.new_index.append(new)
         for _ in self.new_index:
              self.decoded_text+=self.alphabets[_]




              
              
    
    