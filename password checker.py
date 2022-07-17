import requests                            #allow us to make requests to a browser or a site
import hashlib                              #we can perform SHA1 hashing using this library
import re                                   #The re module offers a set of functions that allows us to search a string 
                                            #for a match RegEx can be used to check if a string contains the specified search pattern
 
from colorama import Fore, Style            #This module allow us to produce coloured terminal text   


 
userpassword = input("enter your password:")
 
def request_api_data(query_char):
 
    url = 'https://api.pwnedpasswords.com/range/' + query_char #we got a response of 400 because this API uses hashing,this api also uses the technique of k ananomity
 
    res =  requests.get(url)
    if res.status_code != 200:
      raise RuntimeError(f'error occured: {res.status.code}') #got response 400 which means access is unauthorised or something is wrong with the API
    return res
 
def get_password_leaks_count(hashes,tail):              #in this function, we wil be checking for the leak count of the password
  hashes = (line.split(':') for line in hashes.text.splitlines())       #line.split converts strings to list 
  
  for h, count in  hashes:                              #we will be running a for loop for hashes in which h is the hash key and 
                                                        #count is the no. of times the has key has been leaked
 
    if h==tail:                                         #comparing between hashed key in hashes and tail stored in 'pwned_api_check' function
      print('________________________________________________________________________________\n')
      print(count)
      if int(count)>=1:
        print(Fore.YELLOW + f'{userpassword} ' + Fore.RED +  f'was found {count} times... you should probably change your password!')
        print(Style.RESET_ALL)
        print('________________________________________________________________________________\n')
        break
 
  else:
    print('________________________________________________________________________________\n')
 
    print(Fore.YELLOW + f'{userpassword} ' + Fore.GREEN + 'was NOT found. Carry on!')
    print(Style.RESET_ALL)
 
    print('________________________________________________________________________________\n')


 
password_length = len(userpassword)
 
print('\n________________________________________________________________________________\n')
 
print(f'Your pasword consist of {password_length} characters\n')
 
print('________________________________________________________________________________\n')
 
strength = userpassword                                 
flag = 0                                            #placing the initial value of flag as 0, when the value of flag becomes -1, 
 
while True:                                         #loop breaks
    if (len(strength)<8):
        flag = -1                                        
        break
 
    elif not re.search("[a-z]", strength):          #The re.search() method takes a regular expression pattern and a string
                                                    #and searches for that pattern within the string
        flag = -1
        break
 
    elif not re.search("[A-Z]", strength):
        flag = -1
        break
 
    elif not re.search("[0-9]", strength):
        flag = -1
        break
 
    elif not re.search("[_@#$]", strength):
        flag = -1
        break
 
    elif re.search("\s", strength):
        flag = -1
        break
 
    else:
        flag = 0
        print('Your password ' + Fore.YELLOW + f' {userpassword} ' + Style.RESET_ALL + 'is a ' + Fore.GREEN +  'Strong Password!\n' )
        print(Style.RESET_ALL)
        break
  
if flag ==-1:
    print('Your password ' + Fore.YELLOW + f' {userpassword} ' + Style.RESET_ALL + 'is a ' + Fore.RED +  'Weak Password!\n' )
    print(Style.RESET_ALL)
 
def pwned_api_check(password):  #checks password if it existsin API response (this also converts our password into sha1 hashed password)
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #when added fuction hashlib it hashes the 123 and when used 
                                                                            #hexdigest it converts the hash into SHA1 hash 
  
  first5_char = sha1password[:5] #in this we will be slicing the string the first 5 characters of the password
 
  tail = sha1password[5:]  #in this we will be slicing the string and storing the rest of the characters of the password
 
  response = request_api_data(first5_char)
 
  return get_password_leaks_count(response, tail)
 
pwned_api_check(userpassword)