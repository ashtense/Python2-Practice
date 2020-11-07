class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:

    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self, head):
        currTempNode = head
        while(currTempNode is not None and currTempNode.next is not None):
            if(currTempNode.data==currTempNode.next.data):
                sameValueNode = currTempNode.next
                currTempNode.next = sameValueNode.next
            else:
                currTempNode = currTempNode.next
                

solution_obj = Solution()
arr_input = [1,2,2,3,3,4]
head=None
for arr_index in range(len(arr_input)):
    head = solution_obj.insert(head, arr_input[arr_index])
solution_obj.removeDuplicates(head)
solution_obj.display(head)
