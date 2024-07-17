class RandomizedCollection:
    
    def __init__(self):
        self.d=defaultdict(int)
        self.li=[]
        

    def insert(self, val: int) -> bool:
        self.li.append(val)
        self.d[val]+=1
        if self.d[val]!=1:
            return False
        return True

    def remove(self, val: int) -> bool:
        if self.d[val]!=0:
            self.li.remove(val)
            self.d[val]-=1
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.li)
