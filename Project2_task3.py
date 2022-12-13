import sys

class Node(object):
    def __init__(self, frequency, character = '', left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
        self.huffmanCode = ''

    def get_left(self):
        return self.left

    def get_right(self):
        return self.left
        
def calc_frequency(str):
    symbols = dict()
    for element in str:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols
    
def calc_huffmancode(node, codes = {}, value=''):
    v = value + str(node.huffmanCode)
    if node.get_left():
        calc_huffmancode(node.left, codes, v)
    if node.get_right():
        calc_huffmancode(node.right, codes, v)
    if(not node.get_left() and not node.get_right()):
        codes[node.character] = v
    return codes
    
def print_encoding(data, encoding):
    output = []
    for c in data:
        output.append(encoding[c])  
    string = ''.join([str(item) for item in output])
    return string
    
def huffman_encoding(data):
    # returns -1,-1 if error encounterd
    if data != "":
        if type(data) == str:
            char_freq = calc_frequency(data)
            print(char_freq.items())
            characters = char_freq.keys()
            frequency = char_freq.values()
        
            nodes = []
        
            for c in characters:
                nodes.append(Node(char_freq.get(c), c))

            while len(nodes) > 1:
                nodes = sorted(nodes, key=lambda x: x.frequency)
            
                left = nodes[0]
                right = nodes[1]
            
                left.huffmanCode = 0
                right.huffmanCode = 1
            
                newParentNode = Node(left.frequency + right.frequency, left.character + right.character, left, right)
            
                nodes.remove(left)
                nodes.remove(right)
                nodes.append(newParentNode)
        
            huffman_encoding = calc_huffmancode(nodes[0])
            print(huffman_encoding)
            output = print_encoding(data, huffman_encoding)
            return output, nodes[0]
        else:
            print("\n///////////////////////Input data is type {}. Type must be str./////////////////////////\n".format(type(data)))
            return('-1','-1')
    else:
        print("\n///////////////////////Input cannot be empty/////////////////////////\n".format(type(data)))
        return('-1','-1')


        
def huffman_decoding(input, tree):
    if input != '-1':
        output = []
        target = tree
        for i in input:
            if tree.left == None and tree.right == None:
                output.append(tree.character)
                tree = target
            if i == '0':
                tree = tree.left
            if i == '1':
                tree = tree.right
        output.append(tree.character)
        string = ''.join([str(i) for i in output])
        return string
    else:
        pass
            

# Test Case 1
a_great_sentence = ("AB"*1000)

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # expect 2049
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence) # expect dict_items([('A', 1000), ('B', 1000)]) , {'i': '000', 'r': '001', 'd': '010', 'T': '0110', 'b': '0111', 's': '1000', 't': '1001', 'w': '1010', 'o': '1011', ' ': '110', 'h': '1110', 'e': '1111', 'A': '0', 'B': '1'}

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # expect 292
print ("The content of the encoded data is: {}\n".format(encoded_data)) # too large to put here

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) #expect 2049
print ("The content of the encoded data is: {}\n".format(decoded_data)) # too large to put here


# Test Case 2
a_great_sentence = 12345

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # expect 28
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence) # expect ///////////////////////Input data is type <class 'int'>. Type must be str./////////////////////////

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # expect 28
print ("The content of the encoded data is: {}\n".format(encoded_data)) # expect -1

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # expect 16
print ("The content of the encoded data is: {}\n".format(decoded_data)) # expect None

# Test Case 3
a_great_sentence = ""

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # expect 49
print ("The content of the data is: {}\n".format(a_great_sentence)) # expect ""

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # expect 28
print ("The content of the encoded data is: {}\n".format(encoded_data)) # expect -1

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # expect 16
print ("The content of the encoded data is: {}\n".format(decoded_data)) # expect None

