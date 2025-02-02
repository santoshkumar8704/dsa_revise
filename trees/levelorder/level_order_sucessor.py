from collections import deque
def levelOrderSucessor(root,element):
    q = deque([root])
    elementFound = False
    while q: 
        ele = q.popleft()
        if elementFound:
            return ele.val
        if ele.val == element:
            elementFound = True
        if ele.left:
            q.append(ele.left)
        if ele.right:
            q.append(ele.right)
    return None 


    