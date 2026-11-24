import sys 
def findlargest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3 :
        return n2   
    else :
        return n3 
if __name__ == "__main__":    
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num3 = sys.argv[3]
    print("Largest number is ")
    findlargest(num1,num2,num3)