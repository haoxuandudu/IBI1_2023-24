import re

repeat = input("Enter the repetitive sequence ('GTGTGT' or 'GTCTGT'): ")

if repeat not in ['GTGTGT', 'GTCTGT']:
    print("Invalid repetitive sequence.")
    exit()

filename = f"{repeat}_duplicate_genes.fa"

input_file = 'C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all .fa'

# Open the input file for reading and the output file for writing
with open(input_file, 'r') as input_f, open(filename, 'w') as output_f:
    gene_name = ''
    sequence = ''

    for line in input_f:
        line = line.strip()

        if line.startswith('>'):  # New sequence description
            match = re.search(r'gene:(\S+)', line)
            if gene_name and repeat in sequence:
                # Write the gene's sequence to the output file with modified sequence name
                output_f.write(f'>{gene_name}_{sequence.count(repeat)}\n{sequence}\n')

            # Update the gene name and reset the sequence
            gene_name = match.group(1)
            sequence = ''
        else:
            # Append the sequence to the current gene
            sequence += line

    # Write the last gene's sequence to the output file if it contains the repetitive element
    if gene_name and repeat in sequence:
        output_f.write(f'>{gene_name}_{sequence.count(repeat)}\n{sequence}\n')

print(f"Duplicate genes with repetitive sequence '{repeat}' extracted and saved to '{filename}'")