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
        date = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S.%f %m/%d/%y")
        return date

    # create SHA-256 hash
    def calc_hash(self):

        sha = hashlib.sha256()
                  
        sha.update(str(self.index).encode('utf-8') +
                    str(self.timestamp).encode('utf-8') +
                    str(self.data).encode('utf-8') +
                    str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.chain = []
        self.last_block = None


    def get_last_block(self):
        if len(self.chain) == 0:
            return None
        self.last_block = self.chain[-1]
    

    # create new block
    def create_next_block(self, block, data):
        previous_hash = self.last_block.previous_hash
        if previous_hash != block.previous_hash:
            return -1

        new_block = Block(block.index + 1, data, block.hash)
        self.chain.append(new_block)

    # prints the contents of 
def chain_report(blockchain):
    print("\n\n///////////////// Blockchain \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")

    for block in blockchain:
        print("Timestamp: " + block.timestamp + "\n" +
                     "Data: " + block.data + "\n" +
                     "SHA256 Hash: " + block.hash + "\n" +
                     "Previous Hash: " + block.previous_hash + "\n" +
                     "____________________________________________________________________")

    a=1
    # takes an array of data and creates a blockChain
def create_blockchain(data):

    if len(data) == 0:
        return print("\n\n///////////////// Blockchain \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n" +
                     "\nNo data provided. Blockchain not created!\n" +
                     "____________________________________________________________________\n")

    myChain = BlockChain()

    MAX_SIZE = 100
        
    for element in data:
        if len(element) > MAX_SIZE:
            print("\nData exceeds max character length for hash. Element not included in the blockchain\n" +
                  "____________________________________________________________________\n")
            break

        # create genesis block
        if len(myChain.chain) == 0:
            myChain.chain.append(Block(0, element, "Genesis Block"))
            myChain.get_last_block()

        else:
            myChain.create_next_block(myChain.last_block, element)
            myChain.get_last_block()
    
    return chain_report(myChain.chain)


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

data = ['cat', 'dog', 'bird', 'fish']
create_blockchain(data)


# Test Case 1 - large data value

data = ['cat', 'dog', 'bird', 'fish', 'A'*101] 
create_blockchain(data) # expect blockchain created with no issues

# Test Case 2 - empty dataset
data = []
create_blockchain(data) # expect return -1

# Test Case 3 - duplicate elements in dataset
data = ['cat', 'cat', 'cat', 'cat', 'cat']
create_blockchain(data)# expect blockchain created with no issues
