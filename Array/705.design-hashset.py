class MyHashSet:

    def __init__(self):
        self.hash_set = set()

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.add(key)

        

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hash_set:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

myHashSet  =  MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.contains(1);
myHashSet.contains(3); 
myHashSet.add(2);      
myHashSet.contains(2); 
myHashSet.remove(2);  
myHashSet.contains(2); 