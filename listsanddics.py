def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "jose", "lastname": "naranjo"}

    super_list = [
        {"firstname": "jose", "lastname": "naranjo"},
        {"firstname": "michael", "lastname": "naranjo"},
        {"firstname": "", "lastname": "naranjo"},
        {"firstname": "rodri", "lastname": "naranjo"}
    ]
    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums":[-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 0.5, 6.4]
    }

if __name__ == "__main_":
    run()