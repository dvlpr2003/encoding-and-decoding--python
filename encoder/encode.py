class Encode():
    def __init__(self):
         
         self.alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
         self.text = []
         self.key = None
         self.encoded_text = ""
         self.new_index = [] 
    def update_on_list(self,plain_text,security_key):
         self.key=security_key
         for _ in plain_text:
              self.text.append(_)
        
    def encode(self):
         
         for i in self.text:

            new = self.alphabets.index(i)+self.key
            if new < 26:
                 
                self.new_index.append(new)
            else :
                 new -= 26
                 self.new_index.append(new)


         for _ in self.new_index:
              self.encoded_text+=self.alphabets[_]
  
              






              

         
         
         

         
         