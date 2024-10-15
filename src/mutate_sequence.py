import numpy as np
import copy
import pdb

def mutate_sequence(peptide_sequence, sequence_scores):
    '''Mutate the amino acid sequence randomly
    '''
    restypes = np.array(['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
                 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V' ])
    seqlen = len(peptide_sequence)
    searched_seqs = sequence_scores['sequence']
    for pi in np.random.choice(np.arange(seqlen),seqlen, replace=False):
        for aa in np.random.choice(restypes,len(restypes), replace=False):
            new_seq = peptide_sequence[:pi]+aa+peptide_sequence[pi+1:]
            if new_seq not in searched_seqs:
                return new_seq
