
# O(n * k) time | O(n) space - where n is the height of the staircase and k is the number of allowed steps
def staircaseTraversal(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1
    for currentHeight in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1
    return waysToTop[height]