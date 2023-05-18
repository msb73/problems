class Linklist:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next
head = Linklist(1, Linklist(2,Linklist(3,Linklist(4,Linklist(5, None)))))

print(id(head))
print(id(head.next))
def reversal(head):
    count = 0
    def rec(head, counter, count):
        if counter != count:
            rec(head.next, counter+1, count)
            head.val, head.next.val = head.next.val , head.val
        return head.next
    condition_head = head.next
    while condition_head:
        count +=1
        cond = rec(head,0, count)
        condition_head = condition_head.next
        # a     b       c        d
reversal(head)
# head  next
# if head 
# b     a       c        d
# b     c       a        d
# c     b       a        d

# d     c       b        a
# step 1    reverse   b      a
#               c     b      a
#          d    c     b      a
# suggested a.next = b   head = a
# doing     b.next = a
# suggested b.next = c
# doing     c.next = b
# ~/Documents/python via  v3.10.8 took 32s 