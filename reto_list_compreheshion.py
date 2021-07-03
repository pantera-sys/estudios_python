def run ():
    my_list= [1,2,3,4,5]
    potency=[ i**2 for i  in my_list ]

    print( potency )

if __name__=="__main__":
    run()