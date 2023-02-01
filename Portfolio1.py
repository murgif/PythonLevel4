#!/usr/bin/env python3

import random



if __name__ == '__main__':

    list = ["blue", "yellow", "donkey", "naruto", "metal", "peas", "fish", "vegan", "henry"]
    s = ""
    while True:
        try:
            number = int(input("how many passwords are needed? "))
            if 24< number or number <1 :
                print("Please enter a value between 1 and 24")
            else:
                while number >0 :
                    joined = ((random.sample(list, 3)))
                    print("-->", s.join(joined))
                    number -= 1
        except ValueError:
            print("Please enter a number")
        except KeyboardInterrupt:
            break










