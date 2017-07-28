def to_rna(strand):
    # strand = list(strand)
    # i = 0
    # for i in range (0, len(strand)):
    #     if strand[i] == 'G':
    #         strand[i] = 'C'
    #     elif strand[i] == 'C':
    #         strand[i] = 'G'
    #     elif strand[i] == 'T':
    #         strand[i] = 'A'
    #     elif strand[i] == 'A':
    #         strand[i] = 'U'
    #     else:
    #         return ''
    # return ''.join(strand)

    ##### refactor #####
    rna_dict = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }

    rna_strand = []

    for nucleo in strand:
        if nucleo not in rna_dict:
            return ''
        rna_strand.append(rna_dict[nucleo])
    return ''.join(rna_strand)
