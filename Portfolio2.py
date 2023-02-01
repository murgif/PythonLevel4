#!/usr/bin/env python3
import statistics

def fastest():
    return print(f'Fastest time:', (min(times_list))//60, "minutes,", ((min(times_list))%60), "seconds")
def slowest():
    return print(f'Slowest time:', (max(times_list))//60, "minutes,", ((max(times_list))%60), "seconds")
def total():
    return print("Total runners:", len(runners_list))
def average():
    average = statistics.mean(times_list)
    return print("Average time:", average//60, "minutes,", average%60, "seconds")
def best():

    best = times_list.index(min(times_list))
    return print('Best time here: Runner', runners_list[best])

def ending():
    if len(runners_list) !=0:
        total()
        average()
        fastest()
        slowest()
        print("")
        best()
    else:
        print("No data found. Nothing to do. What a pity.")


if __name__ == "__main__":
    print("Park Run Timer")
    print("~~~~~~~~~~~~~~")
    print("")
    print("Let's go!")

    runners_list = []
    times_list = []
    input_list = []
    list_length = 100

    for idx in range(list_length):
        try:
            item = input('>')
            if item[0].isdigit() and item[-1].isdigit():
                runner, time = item.split('::')
                runners_list.append(int(runner))
                times_list.append(int(time))
            elif item == "end":
                break

            else:
                print("Error in data stream. Ignorning. Carry on")

        except IndexError:
            break
        except ValueError:
            break
    ending()

