import random
import uuid
import time
import sys
sys.setrecursionlimit(1500)

class Node():
    
    def __init__(self, id, payload):
        self.id = id
        self.payload = payload
    
    def return_payload(self):
        return self.payload

    def return_info(self):
        return self.name, self.payload
    
    def request_payload(self, target):
        return target.return_payload()
    
    def request_info(self, target):
        return target.return_info()



all_nodes = {}

for i in range(1000):
    id = uuid.uuid4().hex
    all_nodes[id] = Node(id, random.randint(0,100))

all_keys = list(all_nodes.keys())

start_gossip = time.time()
def gossip(startstep, startid, max_step):
    startnode = all_nodes[startid]
    chosen = {}
    for _ in range(random.randint(2,5)):
        id = random.choice(all_keys)
        chosen[id] = startnode.request_payload(all_nodes[id])
    if startstep == max_step:
        return chosen
    else:
        return [gossip(startstep+1, id, max_step) for i in chosen.keys()]
        
    
startnode = random.choice(all_keys)
print(startnode)
result = gossip(0, startnode, 8)
result_all = {}

# def rec(startstep, elem, res_clients={}):
#     if startstep == 7:
#         for num in elem:
#             res_clients.update(num)
            
#         return res_clients
        
#     for i in elem:
#         rec(startstep+1, i, res_clients)
for i in result:
    for j in i:
        for k in j:
            for l in k:
                for q in l:
                    for w in q:
                        for e in w:
                            for item in e:
                                result_all.update(item)
                          
print(result_all)
keys = list(result_all.keys())
print(len(set(keys)))
# print(f'gossip took {time.time() - start_gossip}')

