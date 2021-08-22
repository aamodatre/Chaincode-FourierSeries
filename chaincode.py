""" 2D boundary determination script """

""" Reference: https://www.geeksforgeeks.org/chain-code-for-2d-line/"""

codeList = [5, 6, 7, 4, -1, 0, 3, 2, 1]
  
# This function generates the chaincode 
# for transition between two neighbour points
def getChainCode(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    hashKey = 3 * dy + dx + 4
    return codeList[hashKey]
  
'''This function generates the list of 
chaincodes for given list of points'''
def generateChainCode(ListOfPoints):
    chainCode = []
    for i in range(len(ListOfPoints) - 1):
        a = ListOfPoints[i]
        b = ListOfPoints[i + 1]
        chainCode.append(getChainCode(a[0], a[1], b[0], b[1]))
    return chainCode