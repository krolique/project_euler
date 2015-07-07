Sub Array Sum
=============

Lets examine the code::

    current_sum = array[0]
    start, end = 0, 0
    while end < len(array):
        if current_sum == desired_sum:
            return array[start:end+1]

        if current_sum <= desired_sum:
            end += 1
            if end < len(array):
                current_sum += array[end]
        else:
            current_sum -= array[start]
            start += 1
    # in the event nothing is found we should return an empty list as per
    # the function contract
    return [] 