import Queue

class graph(object):
    '''Use lists to present a graph
        The list belongs to a nodeX shows the nodes nodeX can reach
        init like this:
            {
                a: [b, c, ...],
                b: [a, e, ...],
                ...
            }
    '''
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict
        self.nodes = graph_dict.keys()
    
    '''Do Breadth First Search to the graph
        s: the start node
        d: the destination
        return the shortest path from s to d, empty if not reachable:
        [s, node1, node2, ..., d]
        
        Breif desc:
            set the nodes undetected: white
            set the nodes first detected: gray
            set the nodes detected: black
            detect the reachable from s, keep gray nodes in a queue
    '''
    def BFS(self, s, d):
        colors = {} #colors of the nodes
        distance = {} #distance of the nodes to s
        parents = {} #parents of the nodes in the detect patch
        detect_queue = Queue.Queue()
        
        # do init work
        for node in self.nodes:
            colors[node] = 'white'
            distance[node] = -1 # set distance -1 to unreachable
            parents[node] = None
        colors[s] = 'gray'
        distance[s] = 0
        detect_queue.put(s)
        
        while not detect_queue.empty():
            gray_node = detect_queue.get()
            reach_list = self.graph_dict[gray_node]
            for node in reach_list:
                if colors[node] == 'white':
                    colors[node] = 'gray'
                    distance[node] = distance[gray_node] + 1
                    parents[node] = gray_node
                    detect_queue.put(node)
            colors[gray_node] = 'black'

        path = []
        if distance[d] == 0:
            path = [s]
        elif distance[d] > 0:
            path = [d]
            parent = d
            while parents[parent] != s:
                parent = parents[parent]
                path.append(parent)
            path.append(s)
            path.reverse()
        else:
            path = []
        return path, distance[d]
            

if __name__ == '__main__':
    g = graph(
      {
        1: [2, 4],
        2: [5],
        3: [5, 6],
        4: [2],
        5: [4],
        6: []
       }
    )
    
    print g.BFS(1, 5)
    print g.BFS(1, 1)
    print g.BFS(3, 2)
    print g.BFS(6, 5)
    
    
    
    from ezpatch.apps.unix_patch.models import TASK_STATUS
    task_status_transition = {
            TASK_STATUS.NEEDSACK_STR: (TASK_STATUS.WORKINPROGRESS_STR,TASK_STATUS.PENDINGIMPLEMENTATION_STR,TASK_STATUS.NEEDMOREINFO_STR,TASK_STATUS.RESOLVED_STR),
            TASK_STATUS.WORKINPROGRESS_STR: (TASK_STATUS.CLOSED_STR,),
            TASK_STATUS.PENDINGIMPLEMENTATION_STR: (),
            TASK_STATUS.NEEDMOREINFO_STR: (),
            TASK_STATUS.PENDING_PLANNED_STR: (),
            TASK_STATUS.RESOLVED_STR: (TASK_STATUS.CLOSED_STR,),
            TASK_STATUS.CLOSED_STR: (),
            TASK_STATUS.CANCELLED_STR: (),
            TASK_STATUS.FORECAST_STR: (),
            TASK_STATUS.INVALID_STR: (),
            TASK_STATUS.PREPARATION_STR: (TASK_STATUS.PENDINGAPPROVAL_STR,TASK_STATUS.CANCELLED_STR),
            TASK_STATUS.PENDINGAPPROVAL_STR: (TASK_STATUS.APPROVED_SCHEDULED_STR,TASK_STATUS.PREPARATION_STR,TASK_STATUS.CANCELLED_STR),
            TASK_STATUS.APPROVED_SCHEDULED_STR: (TASK_STATUS.PREPARATION_STR,TASK_STATUS.READYTOSTART_STR,TASK_STATUS.CANCELLED_STR),
            TASK_STATUS.READYTOSTART_STR: (),
            TASK_STATUS.INPROGRESS_STR: (TASK_STATUS.COMPLETE_STR,TASK_STATUS.APPROVED_SCHEDULED_STR),
            TASK_STATUS.EXPIRED_STR: (),
            TASK_STATUS.REJECTED_STR: (),
            TASK_STATUS.COMPLETE_STR: (TASK_STATUS.CLOSED_STR,)
        }
        
    transition_graph = graph(task_status_transition)
    print transition_graph.BFS(TASK_STATUS.INPROGRESS_STR, TASK_STATUS.CANCELLED_STR)