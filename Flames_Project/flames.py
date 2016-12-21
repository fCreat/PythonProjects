import main


flames = main.Flames()

input = flames.get_input()

def retrieve():
    for each in input:
        yield each

s = retrieve()
name1 = next(s)
name2 = next(s)

n1 = flames.get_names(name1)
n2 = flames.get_names(name2)

if n1 == "Enter valid names." or n2 == "Enter valid names.":
    print "The names you entered is invalid. Please try again."

else:
    l1 = flames.find_length(n1)
    l2 = flames.find_length(n2)

    count = flames.find_common_length(l1, l2, n1, n2)

    word = list("FLAMES")
    length = len(word)

    letter = flames.count_gt_length(count, length, word)

    if len(letter) == 1:
        print flames.flame_selection(letter, name1, name2)
    else:
        print "Both names are same. Enter your name and your partner's name. \nOr \nMay both the names cancel each other."