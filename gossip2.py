import random
import uuid
import time
import sys
sys.setrecursionlimit(1500)

from Node import Node
from AllList import AllList

# generate all nodes
all_nodes = {}
for i in range(1000):
    id = uuid.uuid4().hex
    all_nodes[id] = Node(id, random.randint(0,100))
   
# create a list obj from them 
all_list = AllList(all_nodes)

# added list to each node obj
for node in all_list.get_nodes():
    node.init_alllist(all_list)

result = random.choice(all_list.get_nodes()).gossip(0, 7)

result_dict = {}
for i in result:
    for j in i:
        for k in j:
            for l in k:
                for q in l:
                    for w in q:
                        for e in w:
                            result_dict[w[0]] = w[1]
print(len(list(result_dict.keys())))

