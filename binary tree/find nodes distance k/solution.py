# time = O(n)
# space = O(n)
# find the value from the root
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    nodesDistanceK =[]
    
    findDistanceFromNodeToTarget(tree,target,k,nodesDistanceK)
    return nodesDistanceK
    
def findDistanceFromNodeToTarget(node,target, k, nodesDistanceK):
    if node is None:
        return -1

    if node.value == target:
        addSubtreeNodesAtDistanceK(node, 0, k , nodesDistanceK)
        
        return 1
    
    leftDistance = findDistanceFromNodeToTarget(node.left, target, k , nodesDistanceK)
    rightDistance = findDistanceFromNodeToTarget(node.right, target,k,nodesDistanceK)
    if leftDistance == k or rightDistance ==k:
        nodesDistanceK.append(node.value)
        
    if leftDistance != -1:
        addSubtreeNodesAtDistanceK(node.right, leftDistance+1,k, nodesDistanceK)
        return leftDistance +1 
    if rightDistance != -1:
        addSubtreeNodesAtDistanceK(node.left, rightDistance+1, k, nodesDistanceK)
        return rightDistance+1
    return -1
def addSubtreeNodesAtDistanceK(node,distance,k,nodesDistanceK):
    if node is None:
        return 
    if distance == k:
        nodesDistanceK.append(node.value)
    else:
        addSubtreeNodesAtDistanceK(node.left, distance+1,k, nodesDistanceK)
        addSubtreeNodesAtDistanceK(node.right, distance+1,k,nodesDistanceK)
