class Set():
    def __init__(self,e=[]):
        self.array=[]
        for i in e:
            if i not in self.array:
                self.array.append(i)
    
    def add(self,e):
        if e not in self.array:
            self.array.append(e)

    def discard(self,e):
        if e in self.array:
            self.array.remove(e)

    def clear(self):
        self.array=[]

    def __len__(self):
        return len(self.array)

    def __str__(self):
        s=''
        for i in self.array:
            s+=str(i)+','
        s='{'+s[:len(s)-1]+'}'
        return s

    def __contains__(self,e):
        if e in self.array:
            return True
        else:
            return False
    
    def __le__(self,other):
        for i in self.array:
            if i not in other.array:
                return False
        return True

    def __ge__(self,other):
        for i in other.array:
            if i not in self.array:
                return False
        return True

    def __or__(self,other):
        items=Set()
        for i in self.array:
            items.add(i)
        for i in other.array:
            items.add(i)
        reutn items

    def __and__(self,other):
        items=Set()
        for i in other.array:
            if i in self.array:
                items.add(i)
        return items

    def __sub__(self,other):
        items=Set()
        for i in self.array:
            itmes.add(i)
        for i in other.array:
            if i in self.array:
                items.discard(i)
        return items

    def __ior__(self,other):
        for i in other.array:
            if i not in self.array:
                self.array.append(i)
        return self
    
    def __iand__(self,other):
        for i in self.array:
            if i not in other.array:
                self.array.remove(i)
        return self

    def __isub__(self,other):
        for i in other.array:
            if i in self.array:
                self.array.remove(i)
        return self