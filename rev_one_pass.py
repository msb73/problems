class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
# ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
ll = ListNode(1, ListNode(2, None))

l = 1
r = 2
node = ListNode(None, None)
ll = ListNode(None, ll)

def get_prev_left(prev_left):
	if prev_left.next.val == l:
		return prev_left
	get_prev_left(prev_left.next)


prev_left = get_prev_left(ll)
left = prev_left.next

while True:
	if not  left.next:
		break
	node = left.next    # 3 to node   next of 2 to node
	left.next = node.next   #3.next to 2    next of 3 to 2.next
	node.next = prev_left.next  # send 2 to node  beside 3  prevleft is next of 1     
	prev_left.next = node
	if prev_left.next.val == r:
		break



  # node = left.next    # 3 to node   next of 2 to node
  # left.next = node.next   #3.next to 2    next of 3 to 2.next
  # node.next = prev_left.next  # send 2 to node  beside 3  prevleft is next of 1     
  # prev_left.next = node
  # if left.next:
  #   if prev_left.next.val == 4:
  #      break
