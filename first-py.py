#-------------------------------------------------------------------------------
# Name:        first-py
# Purpose:     test file for atom-plus
#
# Author:      jbot
#
# Created:     04/10/2019
# Copyright:   (c) jammy-bot 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

length_list = []

# initalize the list with i, followed by i plus  i^2 for the number of
# iterations in test_length
def runnit(test_length):
    i=1
    while len(length_list) < test_length:
        length_list.append(i)
        i += i**2
    print(length_list)

runnit(12)

# test a 2nd commit
