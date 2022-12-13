import datetime
import time
import hashlib

# implement Block class
class Block:

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = self.get_gmt_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_hash = None


    # return current date/time in greenwich mean time
    def get_gmt_time(self):
        gmt = time.gmtime(time.time())
        date = date.today().strftime("%m/%d/%y")
        return gmt.tm_hour + ":" + gmt.tm_min + ":" + gmt.tm_sec + " " + date

    # create SHA-256 hash
    def calc_hash(self):

        MAX_SIZE = 100

        if len(self.data) > MAX_SIZE:
            return -1

        sha = hashlib.sha256()
                  
        sha.update(str(self.index).encode('utf-8') +
                    str(self.timestamp).endcode('utf-8') +
                    str(self.data).encode('utf-8') +
                    str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    # create genesis block
    def create_gen_block(self):

        if len(self) > 0:
            return -1

        gen_block = Block(0, "Genesis Block", "0")
        self.head = gen_block
        self.tail = self.head


    # create new block
    def next_block(self, data):

        if len(self) != 0:
            return -1
        
        new_block = Block(self.tail.index + 1, data, self.tail.hash)
        self.tail.next_hash = new_block.hash
        new_block.previous_hash = self.tail.hash
        self.tail = new_block



    #takes an array of data and creates a blockChain
def create_blockChain(data):

    if len(data) == 0:
        return -1

    myChain = BlockChain()
        
    for element in data:
        # create genesis block
        if myChain.head == None:
            myChain.create_gen_block()

        else:
            myChain.next_block(element)
    
    return myChain


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

data = ['cat', 'dog', 'bird', 'fish']
create_blockChain(data)


# Test Case 1 - large data value

data = ['cat', 'dog', 'bird', 'fish', "{}".format("A"*101)] 
create_blockChain(data) # expect blockchain created with no issues

# Test Case 2 - empty dataset
data = []
create_blockChain(data) # expect return -1

# Test Case 3 - duplicate elements in dataset
data = ['cat', 'cat', 'cat', 'cat', 'cat']
create_blockChain(data) # expect blockchain created with no issues
