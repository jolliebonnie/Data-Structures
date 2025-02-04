#time = O(b^2*r)
#space = O(b)
# concs = 1 for loop, 2 nested for loops
def apartmentHunting(blocks,reqs):
    maxDistancesAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i,j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i],closestReqDistance)
        return getIdxAtMinValue(maxDistancesAtBlocks)

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue=array[i]
        if currentValue< minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue

def distanceBetween(a,b): # helper method : for code clarity
    return abs(a-b)