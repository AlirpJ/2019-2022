def main():
    num = 101
    print(primeChecker(num))






def primeChecker(num):
    
    if num > 1:
        
        for i in range(2,int(num)):
            if(num % i) == 0:
                return "Not Prime"
            #else:
                #return "Not Prime"
    else:
        return "Prime"








if __name__ == "__main__":
    main()