# dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#         "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#         "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#         "population": [200.4, 143.5, 1252, 1357, 52.98]}
#
# import pandas as pd
#
# brics = pd.DataFrame(dict)
# print(brics)
import sys

list = ['f', 'l', 'a', 'm', 'e', 's']
print list
length = len(list)
count = 8
index = 0


# noinspection PyUnreachableCode
def remove_flames(count, length, list):
    if count > length:
        index = (count % length) - 1
        del list[index]
        if index < 0:
            list = list
        else:
            list = list[index:] + list[:index]
        length = len(list)
        if length > 1:
            remove_flames(count, length, list)
            return list
        # else:
        #     return list
    # elif count <= length:
    #     index = count - 1
    #     del list[index]
    #     if index < 0:
    #         list = list
    #     else:
    #         list = list[index:] + list[:index]
    #     length = len(list)
    #     if length > 1:
    #         remove_flames(count, length, list)
    #     else:
    #         return list
    #         sys.exit()
            # sys.exitfunc()
    # elif count == length:
    #     index = count - 1
    #     del list[index]
    #     if index < 0:
    #         list = list
    #     else:
    #         list = list[index:] + list[:index]
    #     length = len(list)
    #     if length > 1:
    #         remove_flames(count, length, list)
    #     else:
    #         return list
    #         sys.exit()
    # else:
    #     return list

print remove_flames(8, length, list)
