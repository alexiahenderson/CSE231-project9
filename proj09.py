'''
Author: Alexia Henderson
Project: CSE231 Project 9
Purpose:  crack passwords, examine common patterns
in these passwords, and calculate their entropies.

'''
import math
from math import log2
from operator import itemgetter
from hashlib import md5
import string
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def open_file(message): 
    
    if message == "": #if message is empty, open and return default file
        fileopen = open("pass.txt", "r")
        return fileopen

    while True: #iterates through until sufficient filename is provided
        filename = input(message)
        if filename == "":
            filename = "pass.txt"
            fileopen = open("pass.txt", "r")
            break
        else:
            try: #if message is not blank, attempt to open filename of user input
                fileopen = open(filename, "r")
                break
            except FileNotFoundError:
                print("file not found, try again.")
    return fileopen


            
def check_characters(password, characters):
    
    for i in range(0, len(password)): #iterates from 0 to the end of the password
        if password[i] in characters:
            return True
    return False


def password_entropy_calculator(password):
    l = len(password)
    #sets check variables to see if certain characters are in the string
    check_digit = check_characters(password, string.digits)
    check_punct = check_characters(password, string.punctuation)
    check_upper = check_characters(password, string.ascii_uppercase)
    check_lower = check_characters(password, string.ascii_lowercase)
    
    if password == "": #if password is blank, score is set to zero
        return 0
    if check_digit == True: #only digits in the string, values are calculated
        if check_punct == check_upper == check_lower == False:
            N = 10 #n value represents number of possible symbols
            log_part = math.log2(N) #log of n
            entropy = l * log_part #entropy formula
            return float(round(entropy, 2)) #returns entropy as a float rounded to 2 places
        
    if check_punct == True: #only punctuation, values are calculated
        if check_digit == check_upper == check_lower == False:
            N = 32
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_punct == check_digit == True: #punctuation and digits are in the string
        if check_upper == check_lower == False:
            N = 42
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == True: #only lowercase values in the string
        if check_upper == check_punct == check_digit == False:
            N = 26
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_upper == True: #only uppercase values in the string
        if check_lower == check_digit == check_punct == False:
            N = 26
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == check_upper == True: #lower and uppercase values in the string
        if check_punct == check_digit == False:
            N = 52
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == check_digit == True: #lowercase and digits in the string
        if check_upper == check_punct == False:
            N = 36
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_upper == check_digit == True: #uppercase and digits in the string
        if check_lower == check_punct == False:
            N = 36
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_upper == check_punct == True: #punctuation and uppercase in the string
        if check_lower == check_digit == False:
            N = 58
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == check_punct == True: #lowercase and punctuation in the string
        if check_upper == check_digit == False:
            N = 58
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == check_digit == check_punct == True:
        if check_upper == False: #everything but uppercase values in the string
            N = 68
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_upper == check_digit == check_punct == True:
        if check_lower == False: #everything but lowercase values in the string
            N = 68
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == check_digit == check_upper == True:
        if check_punct == False: #everything but punctuation in the string
            N = 62
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower == check_upper == check_punct == True:
        if check_digit == False: #everything but digits in the string
            N = 84
            log_part = math.log2(N)
            entropy = l * log_part
            return float(round(entropy, 2))
        
    if check_lower and check_digit and check_punct and check_upper == True:
        #every possible type is in the string
        N = 94
        log_part = math.log2(N)
        entropy = l * log_part
        return float(round(entropy, 2))

    


def build_password_dictionary(fp):
    pass_dict = {} #create empty dict
    rank  = 0 #initialize rank 
    for password in fp: #iterate through fp
        password = password.replace("\n", "")
        hash_code = md5(password.encode()).hexdigest() #computer md5 hash
        if hash_code not in pass_dict:
            p_entropy = password_entropy_calculator(password)
            rank += 1
            pass_dict[hash_code] = (password, rank, p_entropy)
        
    return pass_dict

def cracking(fp,hash_D):

    initial_lst = [] # [ (hash, password, entropy), .....]
    cr_count = 0 #initializes cracked password count
    uncr_count = 0 #initialized uncracked password count
    
    for hash_data in fp:
        hash_data = hash_data.split(":")
        hash_data = hash_data[0]
        
#        initial_list.append(hash_tuple)
        if hash_data in hash_D:
            
            tup_val = hash_D.get(hash_data)
            tup = (hash_data, tup_val[0], tup_val[2]) 
            initial_lst.append( tup ) 
            
            cr_count +=1
        else:
            uncr_count += 1
        
    
    initial_lst = sorted(initial_lst, key=itemgetter(1))
    
    return initial_lst, cr_count, uncr_count
        
        

def create_set(fp):  
    '''Read file and return data as a set'''
    create_list = [] #initializes list
    for word in fp:
        word=word.split()
        for x in word: #iterates through each character
            continue
            
        else:
            create_list.append(x)
            
    return set(create_list) #returns data as a set
            

def common_patterns(D,common,names,phrases):
    '''Put your docstring here'''
    pw_dict = {}
    
    for line in D.values():
        pw = line[0]
        pw = pw.lower()
        pw_dict[pw] = set()
        for data in common:
            data = data.lower()
            if data in pw:
                pw_dict[pw].add(data)
        for data in names:
            data = data.lower()
            if data in pw:
                pw_dict[pw].add(data)
        for data in phrases:
            data = data.lower()
            if data in pw:
                pw_dict[pw].add(data)
        pw_dict[pw] = list(pw_dict[pw])
        pw_dict[pw].sort()
    return pw_dict
        
                
        
                
def main():
    '''Put your docstring here'''
    
    BANNER = """
       -Password Analysis-

          ____
         , =, ( _________
         | ='  (VvvVvV--'
         |____(


    https://security.cse.msu.edu/
    """

    MENU = '''
    [ 1 ] Crack MD5 password hashes
    [ 2 ] Locate common patterns
    [ 3 ] Calculate entropy of a password
    [ 4 ] Exit

    [ ? ] Enter choice: '''
    print(BANNER)
    print(MENU)
    while True:
        user_ask = input()
        if user_ask == '1':
            fp = open_file("Common passwords file [enter for default]:")
            hash_D = open_file(" Hashes file: ")
            build_dict = build_password_dictionary(fp)
            
            
            p_list,cracked,uncracked = cracking(hash_D, build_dict)
            print("Cracked Passwords:")
            for data in p_list:
                print('[ + ] {:<12s} {:<34s} {:<14s} {:.2f}'.format('crack3d!', data[0], data[1], data[2]))
            print( '[ i ] stats: cracked {:,d}; uncracked {:,d}'.format(cracked, uncracked))
        elif user_ask == '2':
            file1 = open_file("Common passwords file [enter for default]: ")
            D = build_password_dictionary(file1)
            common = open_file('Common English Words file: ')
            names = open_file('First names file: ')
            phrases = open_file('Phrases file: ')
            common = create_set(common)
            phrases = create_set(phrases)
            names = create_set(names)
            common_p = common_patterns(D, common, names, phrases)
            print("{:20s}{}".format("Password ","Patterns"))
            for k, v in common_p.items():
                print("{:20s} [".format(k),end='')# print password
                print(', '.join(v),end=']\n') # print comma separated list
            
        elif user_ask == '3':
            pw = input('Enter the password: ')
            cpe = password_entropy_calculator(pw)
            print('The entropy of {} is {}'.format(pw, cpe))
        elif user_ask == '4':
#            print("Goodbye.")
            break
            
        else:
            print("Error. Try again.")
        
        print(MENU)
    
if __name__ == '__main__':
    main()
