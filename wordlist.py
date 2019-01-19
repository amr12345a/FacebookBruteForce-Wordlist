from os import path

Email = raw_input('\033[35mEnter username : ')

def createFile(dest):

 name = "passwords.txt"
 x = 100000
 y = str(x)
 print ("""

    12/16/2018
    By

     \033[34m ____    ___ ___    ____
     \033[31m|    |  |   |   |  |    |
     \033[32m|____|  |   |   |  |----
     \033[33m|    |  |       |  |   |
     
  """)

 if not path.isfile(dest):
     
     
     fol = open(dest + "\\" +name,"w" )
     while x < 999999:
         x = x + 1
         fol.write(str(x)+ (2*Email[0]) + "\n")
         fol.write(str(x)+ Email[0:2] + "\n")
         fol.write(Email[0:2]+str(x) + "\n")
     fol.write(3 * Email[0] + 3 * Email[1] + "\n")
     fol.close()
     print("\033[32mdone")
  

if __name__ == '__main__':
  createFile(path.abspath(path.curdir))
  
