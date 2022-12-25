def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    ans = 0
    while len(list1) > i:
        if list1[0] == list1[i]:
            ans += 1
       
        i += 1
    return ans == len(list1)