# Names of all students corresponding with their learning team number.


def solution_station_5(name):
    name_dict = {
        "Soelie": 3,
        "Yasmin": 1,
        "Arnav": 3,
        "Iris" : 2,
        "Lora" : 2,
        "Minseo" : 2
    }

    return name_dict.get(name)