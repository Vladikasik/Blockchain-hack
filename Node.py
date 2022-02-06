import random

class Node():
    
    def __init__(self, id, payload):
        self.id = id
        self.payload = payload
        self.all_list = None
        
    def init_alllist(self, all_list):
        self.all_list = all_list
    
    def return_payload(self):
        return self.payload

    def return_info(self):
        return self.id, self.payload
    
    def gossip(self, current_step, max_step):
        if current_step == max_step:
            return self.return_info()
        else:
            pick = lambda: random.choice(self.all_list.get_nodes())
            def node_rungos(node_id):
                node = self.all_list.get_Node(node_id)
                return node.gossip(current_step+1, max_step)
            picked = [pick() for _ in range(random.randint(2,5))]
            return [node_rungos(node.id) for node in picked]