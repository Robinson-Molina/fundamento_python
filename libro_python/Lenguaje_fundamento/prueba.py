for n in range(2,10):
    x=2
    while x < n:
        if n % x == 0:
            print('%i vale %i * %i' % (n,x,n/x))
            break
        #print(x)
        x += 1
    else:
        print('%i es un numero primo' %n)

#·for i in range(1, 50962):
#    print("numero",i,":"); print(chr(i))