class Item:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box:

    def add(self):
        pass

    def empty(self):
        pass

    def count(self):
        pass

class ListBox(Box):

    def __init__(self):
        self.BoxList = []

    def add(self, item):
        self.BoxList.append(item)

    def empty(self):
        self.BoxList = []

    def count(self):
        return len(self.BoxList)

class DictBox(Box):

    def __init__(self):
        self.BoxDict = dict()

    def add(self, item):
        self.BoxDict[item.name] = item.value

    def empty(self):
        self.BoxDict = dict()

    def count(self):
        return len(self.BoxDict)

item1 = Item("a", 3)
item2 = Item("b", 4)
item3 = Item("c", 5)
boxes_list = ListBox()
boxes_dict = DictBox()

boxes_list.add(item1)
boxes_list.add(item2)
boxes_list.empty()
boxes_list.add(item3)
print(boxes_list.count())

boxes_dict.add(item1)
boxes_dict.add(item2)
boxes_dict.add(item3)
print(boxes_dict.count())
