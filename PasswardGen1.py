import string
import random
if __name__ == '__main__':


    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    len=int(input("Enter The Passward Length\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("Your Passward Is :  \n")
    pass1="".join(random.sample(s,len)) 
    print(pass1)
    f=open("Pass.txt","a")
    f.write(pass1)
    f.write("\n")
    f.close()