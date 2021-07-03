def run():
    print("hola")
    squares= [i**2 for i in range(1, 101) if i %3 != 0]
    divisibles = [i**2 for i in range(1, 101) if i %3 == 0]
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i)
    #     else:
    #         divisibles.append(i)
    print(squares)
    print(divisibles)



if __name__ == "__main__":
    run()
