from Node import Node
from typing import List, Dict  # For annotations
from colorama import Fore, Style

class Graph:

    def __init__(self, source: int, adj_list: Dict[int, List[int]]):
        if source < 1 or source > len(adj_list) :
            raise Exception(Fore.LIGHTYELLOW_EX + f"ERROR, Choose node between 1 to {len(adj_list)}")
            print(Style.RESET_ALL, end='')
        else:
            self.source = source - 1
            self.adjlist = adj_list

    def Prim_MST(self) -> int:
        MST =[]
        # Priority queue is implemented as a dictionary with
        # key as an object of 'Node' class and value as the cost of
        # reaching the node from the source.
        # Since the priority queue can have multiple entries for the
        # same adjacent node but a different cost, we have to use objects as
        # keys so that they can be stored in a dictionary.
        # [As dictionary can't have duplicate keys so objectify the key]

        # The distance of source node from itself is 0. Add source node as the first node
        # in the priority queue
        priority_queue = {Node(self.source): 0}
        visited = [False] * len(self.adjlist)
        min_span_tree_cost = 0
        print(Fore.LIGHTYELLOW_EX + "\t P R I M ' S \t M S T")
        print(Style.RESET_ALL, end='')
        """ PRIM'S SHORTEST PATH ALGORITHM """
        while priority_queue:
            # Choose the adjacent node with the least edge cost
            node = min(priority_queue, key=priority_queue.get)  # min priority queue
            cost = priority_queue[node]
            # Remove the node from the priority queue
            del priority_queue[node]
            if visited[node._id] == False:
                min_span_tree_cost += cost
                visited[node._id] = True
                print("Added Node (" + str(node._id) + "), Parent Node (" + str(node.parent) +"), cost now : " + str(
                    min_span_tree_cost) + ", Edge weight : " + str(cost))
                MST.append([node.parent, node._id, cost])

                for item in self.adjlist[node._id]:
                    adjnode = item[0]
                    adjcost = item[1]
                    if visited[adjnode] == False:
                        vertex = Node(adjnode)
                        priority_queue[vertex] = adjcost
                        vertex.parent = node._id
        """ END """
        return MST

    def Dijkstra_MST(self) -> int:
        MST = [[None, 0, 0]]  # for printing

        priority_queue = {Node(self.source): 0}
        distance = [False] * len(self.adjlist)
        distance[0] = 0
        print(Fore.LIGHTYELLOW_EX + "\t D I J K S T R A ' S \t M S T")
        print(Style.RESET_ALL, end='')

        """ DIJKSTRA'S SHORTEST PATH ALGORITHM """
        while priority_queue:
            # Choose the adjacent node with the least edge cost
            node = min(priority_queue, key=priority_queue.get)  # min priority queue
            # Remove the node from the priority queue
            del priority_queue[node]
            # get all the adjacent
            for item in self.adjlist[node._id]:
                adjnode = item[0]
                adjcost = item[1]
                if distance[adjnode] is False or distance[adjnode] > distance[node._id] + adjcost:
                    vertex = Node(adjnode)
                    vertex.parent = node._id
                    distance[adjnode] = distance[node._id] + adjcost
                    priority_queue[vertex] = adjcost
                    """ END """

                    flag = False
                    for element in MST:
                        if element[1] == adjnode:
                            flag = True
                            break
                    if flag:
                        element[0] = node._id
                        element[2] = adjcost
                    else:
                        MST.append([node._id, adjnode, adjcost])

        # return min_span_tree_cost
        for i in range(len(self.adjlist)):
            print("Source Node (" + str(self.source + 1) + ")  -> Destination Node(" + str(i + 1) + ")  : "
                  + str(distance[i]))
        return MST

