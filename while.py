#INPUT => 7

#OUTPUT =>

def main():
    size = int(input())
    i = 1
    
    #untuk setiap i sebanyak size 
    #selama kondisi i < size adalah TRUE
    while i <= size:
        j = size
        while j >= i:
            print('*', end='')
            j -= 1
        print('')  
        i += 1
        
#untuk memastikan bahwa name dari program ini adalah __main__
if __name__ == '__main__':
    main()

