# # def list_benefits():
# #     return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# #
# # # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# # def build_sentence(benefit):
# #     return "%s is a benefit of functions!" % benefit
# #
# #
# # def name_the_benefits_of_functions():
# #     list_of_benefits = list_benefits()
# #     for benefit in list_of_benefits:
# #         print(build_sentence(benefit))
# #
# # name_the_benefits_of_functions()
# #
# #
# # def fib(n):
# #     if n == 0:
# #         return 0
# #     if n == 1:
# #         return 1
# #     return fib(n-1)+fib(n+1)
#
# # def generatenumber(n):
# #     return range(0, n, 1)
#
# # print(generatenumber(10))
# def generatenumber():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
# g = generatenumber()
#
# print(next(g))
#
# print(next(g))
# print(next(g))


# #
# # for i in g:
# #     if i > 20:
# #        break
# #     print i
#
#
# def hello():
#     while True:
#         y = (yield)
#         print y
#
# h = hello()
# h.send(None)
# h.send("hi")
# h.send("pavan")
# h.send("baskar")
# h.send("karthik")
# h.close()
#
# def sum(*args):
#     return reduce(lambda a,b: a+b, args)
#
# print sum(1,23,3)
#
# def keyword(*args, **kwds):
#     print(kwds)
#
# print keyword(1, 2, 3)
# print keyword(a=1,b=2, c=3)
# logging(length(1,2,3))
# def logging(f):
#     def inner(*args):
#         print "Input is {}".format(args)
#         res = f(*args)
#         print "Output is {}".format(res)
#         return res
#     return inner

# # func1(func2())
#
# @logging
# def length(*args):
#     return len(args)

#
# # logging -> f = inner
# # f () as input and int as output
# #
#
# #f(x)  =>  y
# # g(y) => z
#
# g(f())
#
# length(1,2,3,4)
#
#
# # reference couting
#
#

# a = 1
# b = 2
#
# print(id(a))
# print(id(b))

#threading

print 2 % 5