#import marvellous     
#from marvellous import *    #direct call karcha addition fun() te marvellous file madhe ahe
import marvellous as M
import infosystem

def main():
    print("inside module:",__name__);

    no1=int(input("enter the no 1="));      #10
    no2=int(input("enter the no 2="));      #11

    ret =M.addition(no1, no2);              #addition(10,11)
    print("additon is=",ret);    

    #infosytem file
    ret2 = infosystem.subtraction(no1, no2);              #subtraction(10,11)
    print("subtraction is=",ret2);          
    
if __name__=="__main__":                #startter code ithun chalu honar
    main()