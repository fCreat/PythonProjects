class Flames(object):

    def get_input(self):
        n1 = raw_input("Enter your name: ")
        n2 = raw_input("Enter your partner's name: ")
        return n1, n2


    def get_names(self, name1):
        self.name1 = name1.lower()
        self.name1 = self.name1.replace(" ", "")
        if self.name1.isalpha():
            return list(self.name1)
        else:
            return "Enter valid names."


    def find_length(self, list):
        lnt = len(list)
        return lnt

    def find_common_length(self, l1, l2, name1, name2):
        for i in range(0, l1):
            for j in range(0, l2):
                try:
                    if name1[i] == name2[j]:
                        name1.remove(name1[i])
                        name2.remove(name2[j])

                    else:
                        continue

                except IndexError:
                    l1 -= 1
                    l2 -= 1
                    self.find_common_length(l1, l2, name1, name2)

        return len(name1) + len(name2)

    def count_gt_length(self, count, length, list):
        if count == 0:
            return list
        else:
            while count >= length or count <= length:
                index = (count % length) - 1
                del list[index]
                length = len(list)
                if index >= 1:
                    list = list[index:] + list[:index]
                    continue
                else:
                    list = list
                    if length == 1:
                        break
        return list

    def flame_selection(self, letter, name1, name2):

        for x in letter:
            if x == 'A':
                return "%s and %s has got \'A\' which stands for AFFECTION." % (name1, name2)
            elif x == 'F':
                return "%s and %s has got \'F\' which stands for FRIENDS." % (name1, name2)
            elif x == 'L':
                return "%s and %s has got \'L\' which stands for LOVE." % (name1, name2)
            elif x == 'M':
                return "%s and %s has got \'M\' which stands for MARRIAGE." % (name1, name2)
            elif x == 'E':
                return "%s and %s has got \'E\' which stands for ENEMY." % (name1, name2)
            else:
                return "%s and %s has got \'S\' which stands for SIBLING." % (name1, name2)
