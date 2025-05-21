class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not isinstance(obj, ObjList):
            raise TypeError("obj is not instance in ObjList")
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            return None
        removed = self.tail
        prev_node = removed.get_prev()

        if prev_node is None:
            self.head = None
            self.tail = None
        else:
            prev_node.set_next(None)
            self.tail = prev_node

        removed.set_prev(None)
        removed.set_next(None)
        return removed

    def get_data(self):
        res = []
        cur = self.head
        while cur is not None:
            res.append(cur.get_data())
            cur = cur.get_next()
        return res


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, obj):
        self.__next = obj

    def get_next(self):
        return self.__next

    def set_prev(self, obj):
        self.__prev = obj

    def get_prev(self):
        return self.__prev

