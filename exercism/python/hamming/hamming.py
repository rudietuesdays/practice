def distance(strand_1, strand_2):
    if len(strand_1) != len(strand_2):
        raise ValueError
    # if strand_1 == strand_2:
    #     return 0
    # count = 0
    # for i in range (0, len(strand_1)):
    #     if strand_1[i] != strand_2[i]:
    #         count += 1
    # return count

    ##### refactor #####

    return len([1 for x, y in zip(strand_1, strand_2)  if x != y])
