def main():
    size = int(input())

    #for loop
    #untuk setiap i dari 0 s.d. size 
    for i in range(0, size):
        #untuk setiap j dari 0 s.d. 1
        for j in range(0, i):
            print('*', end='')
            #break line
        print('')
    
#untuk memastikan bahwa name dari program ini adalah __main__ 
if __name__=='__main__':
    main()
