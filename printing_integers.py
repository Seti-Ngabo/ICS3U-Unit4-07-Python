#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program uses a nested loop


def main():
    # this function uses a nested loop

    # process & output
    for counter in range(1000, 2001):
        if counter % 5 == 4:
            print("{}".format(counter))
        else:
            print("{} ".format(counter), end="")


if __name__ == "__main__":
    main()
