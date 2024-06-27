# Prompt user to input DNA sequence
dna_seq = input("Enter DNA sequence: ")
#Changing every base with it's complementary base, So A will bind with T and C will bind with G.
# Transcribes a DNA sequence to RNA by replacing 'T' with 'U'.
# T stands for the nitrogenous base thymine & U stands for the uracil
#Uracil and thymine have a  similar chemical structure. The only difference between them is the presence of an
#  extra methyl group in the thymine structure.
# 'C' will be temporarily replaced with 'X' before 'G' is replaced with 'C', and then 'X' will be replaced with 'G', 
# resulting in the correct mRNA sequence.
def dna_to_mrna(dna_seq):
    rna_seq = dna_seq.upper().replace('A', 'U').replace('T', 'A').replace('C', 'X').replace('G', 'C').replace('X', 'G')   
    return rna_seq


# Transcribe DNA to mRNA
mrna_seq = dna_to_mrna(dna_seq)

# ensure that the mRNA sequence is divisible by 3 bcuz each sequence of three bases codes for one amino acid
if len(mrna_seq) % 3 != 0:
        raise ValueError("Frameshift Mutation detected!! The mutation is either Insertion or Deletion")

# define the standard genetic code as a dictionary , dictionary of all the 20 amino acids
genetic_code ={"UUU": "Phe-", "UUC": "Phe-", "UUA": "Leu-", "UUG": "Leu-",
"UCU": "Ser-", "UCC": "Ser-", "UCA": "Ser-", "UCG": "Ser-",
"UAU": "Tyr-", "UAC": "Tyr-", "UAA": "Stp-", "UAG": "Stp-",
"UGU": "Cys-", "UGC": "Cys-", "UGA": "Stp-", "UGG": "Trp-",
"CUU": "Leu-", "CUC": "Leu-", "CUA": "Leu-", "CUG": "Leu-",
"CCU": "Pro-", "CCC": "Pro-", "CCA": "Pro-", "CCG": "Pro-",
"CAU": "His-", "CAC": "His-", "CAA": "Gln-", "CAG": "Gln-",
"CGU": "Arg-", "CGC": "Arg-", "CGA": "Arg-", "CGG": "Arg-",
"AUU": "Ile-", "AUC": "Ile-", "AUA": "Ile-", "AUG": "Met-",
"ACU": "Thr-", "ACC": "Thr-", "ACA": "Thr-", "ACG": "Thr-",
"AAU": "Asn-", "AAC": "Asn-", "AAA": "Lys-", "AAG": "Lys-",
"AGU": "Ser-", "AGC": "Ser-", "AGA": "Arg-", "AGG": "Arg-",
"GUU": "Val-", "GUC": "Val-", "GUA": "Val-", "GUG": "Val-",
"GCU": "Ala-", "GCC": "Ala-", "GCA": "Ala-", "GCG": "Ala-",
"GAU": "Asp-", "GAC": "Asp-", "GAA": "Glu-", "GAG": "Glu-",
"GGU": "Gly-", "GGC": "Gly-", "GGA": "Gly-", "GGG": "Gly-"
}


def translate_mrna(mrna_seq):
    
    
    
    # iterate over the mRNA sequence, translating each 3 letter codon to an amino acid symbol
    aa_seq = ""
    for i in range(0, len(mrna_seq), 3):
        codon = mrna_seq[i:i+3]
        aa = genetic_code.get(codon, None)
        if aa is None:
            raise ValueError("invalid codon: {}".format(codon))
        aa_seq += aa
    
    return aa_seq
aa_seq = translate_mrna(mrna_seq)



aa_names={
  "Ala-": "Alanine-",
  "Arg-": "Arginine-",
  "Asn-": "Asparagine-",
  "Asp-": "Aspartic acid-",
  "Cys-": "Cysteine-",
  "Gln-": "Glutamine-",
  "Glu-": "Glutamic acid-",
  "Gly-": "Glycine-",
  "His-": "Histidine-",
  "Ile-": "Isoleucine-",
  "Leu-": "Leucine-",
  "Lys-": "Lysine-",
  "Met-": "Methionine-",
  "Phe-": "Phenylalanine-",
  "Pro-": "Proline-",
  "Ser-": "Serine-",
  "Thr-": "Threonine-",
  "Trp-": "Tryptophan-",
  "Tyr-": "Tyrosine-",
  "Val-": "Valine-"
}



   
def convert_aa_symbols_to_names(aa_seq):
    
    
    
    # iterate over the mRNA sequence, translating each 3 letter codon to an amino acid symbol
     aa_seqfull = str("")
     for i in range(0, len(aa_seq),4):
        codon = aa_seq[i:i+4]
        aas = aa_names.get(codon, None)
        aa_seqfull += aas
     return aa_seqfull

aa_seqfull = convert_aa_symbols_to_names(aa_seq)        

# print the result
print(f"\n mRNA sequence:  \n{mrna_seq}")


print(f"\nAmino acids symbols:{aa_seq} \n")

print(f"\nAmino acid names:{aa_seqfull} \n")
