def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i = 0
    while len(list1)>i:
        if list1[i] == 1:
            list1[i] = True
        i += 1
    return list1