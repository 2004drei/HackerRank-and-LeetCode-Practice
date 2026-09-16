def mergeTwoLists(list1, list2):
  """
  :type list1: Optional[ListNode]
  :type list2: Optional[ListNode]
  :rtype: Optional[ListNode]
  """
  def to_list(node):
    result = []
    while node:
      result.append(node.val)
      node = node.next
    return result

  mergedList = sorted(to_list(list1) + to_list(list2))

  # dummy = ListNode(0)
  # current = dummy
  # for val in mergedList:
  #   current.next = ListNode(val)
  #   current = current.next

  # return dummy.next
