from types import NoneType


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):
    # initialize class variables
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.cache = {}
        self.capactiy = capacity
        self.size = 0

    # remove node from current location
    def eviction(self,node):
        if node == self.head:
            self.head = node.next
            node.previous = None
        
        elif node == self.tail:
            pass

        else:
            previous = node.previous
            nxt = node.next
            node.previous.next = nxt
            node.next.previous = previous

    # move most recently used node to the back of the line
    def relocation(self,node):
        current_tail = self.tail
        node.previous = current_tail
        current_tail.next = node
        self.tail = node
        node.next = None

    # retrieve node via key if cache hit, return -1 if cache miss
    def get(self, key):
        if key not in self.cache:
            return -1
      
        node = self.cache[key]
        self.eviction(node)
        self.relocation(node)
        return node.value

    # add new node to the cache
    def set(self, key, value):

        if type(key) != NoneType or type(value) != NoneType:

            if self.head is None:
                new_node = Node(key, value)
                self.cache[key] = new_node
                self.head = new_node
                self.tail = self.head
                self.size += 1

            elif key in self.cache:
                node = self.cache[key]
                node.value = value
                self.eviction(node)
                self.relocation(node)   
            else:
                if self.size >= self.capactiy:
                    node = self.head
                    del self.cache[node.key]
                    self.eviction(node)
                    self.size -=1

                new_node = Node(key, value)
                self.cache[key] = new_node
                self.relocation(new_node)
                self.size += 1
            return "Action complete!"

        else:
            return -1



our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.set(1, 1);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
new_cache = LRU_Cache(2)
print(new_cache.set(None,None)) # expect -1
print(new_cache.get(None)) # expect -1


# Test Case 2
new_cache = LRU_Cache(2)
print(new_cache.set(10000*10000, 10000000*10000000)) # expect "Action Complete!"
print(new_cache.get(10000*10000)) # expect 100000000000000

# Test Case 3
new_cache = LRU_Cache(1)
print(new_cache.set(-2,-2)) # expect "Action Complete!"
print(new_cache.get(-2)) # expect -2
