def run():
    multiples=[i for i in range(1, 100000) if i % 4 ==0 and  i % 6 ==0 and  i % 9 ==0]
 
    # for i in range(1, 1000000):
    #     if i % 4 ==0 and if i % 6 ==0 and if i % 9 ==0:
    print(multiples)
if __name__ == "__main__":
    run()

