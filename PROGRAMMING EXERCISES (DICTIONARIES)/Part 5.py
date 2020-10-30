def K_mer(DNA, k=0):
    count = {}
    for x in range(len(DNA)):
        kmer = DNA[x:(x+k)]
        count[kmer] = count.get(kmer, 0) + 1
    return count

def main():
    DNA = 'GTAGTAGAAGAGGAGCAGCTGCTGCTGT'
    print(K_mer(DNA,k=2))

main()