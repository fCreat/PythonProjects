# #
# # list = ['f', 'l', 'a', 'm', 'e', 's']
# #
# # length = len(list)
# #
# # count = 7
# #
# # # while count > length:
# # #     index = (count % length) - 1
# # #     del list[index]
# # #     length = len(list)
# # #     if index >= 1:
# # #         list = list[index:] + list[:index]
# # #         continue
# # #     else:
# # #         list = list
# # #         if length == 1:
# # #             break
# #
# #
# #
# # def count_gt_length(count, length, list):
# #     while count >= length or count <= length:
# #         index = (count % length) - 1
# #         del list[index]
# #         length = len(list)
# #         if index >= 1:
# #             list = list[index:] + list[:index]
# #             continue
# #         else:
# #             list = list
# #             if length == 1:
# #                 break
# #     return list
# #
# # print count_gt_length(8, 6, list)
#
#
# class encapsulation(object):
#
#     def __init__(self, max, min):
#         self.max = max
#         self.min = min
#
#     def __str__(self):
#         return str(self.max) + ' + ' + str(self.min)
#
# __maxi = 100
# __mini = 200
#
# enc = encapsulation(__maxi, __mini)
# print enc
#

# class Bhasker(object):
#
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def addd(self, a, b):
#         return self.a + self.b

# a = raw_input("Enter a value: ")
# print type(a)
# try:
#     if int(a) >= 0 or int(a) < 0:
#         print "it is an integer"
#
# except ValueError:
#     print "Not an integer"
#
# print '%s' %(a)

def func(ash, *args, **kwargs):
    print ash
    print args
    print kwargs

func("Surya", 1, 2,3, 4, 5, {"a": 5, "b" : 6})