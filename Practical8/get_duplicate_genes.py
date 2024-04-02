import re
input_file = 'C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all .fa'
output_file = 'C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical8/duplicate_genes.fa'

# Open the input file for reading and the output file for writing
with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
    gene_name = ''
    sequence = ''

    for line in input_f:
        line = line.strip()

        if line.startswith('>'):  
            match = re.search(r'gene:(\S+)', line)
            if match and 'duplication' in line:
                if gene_name:
                    # Write the previous gene's sequence to the output file
                    output_f.write(f'>{gene_name}\n{sequence}\n')

                # Update the gene name and reset the sequence
                gene_name = match.group(1)
                sequence = ''
        else:
            # Append the sequence to the current gene
            sequence += line

    # Write the last gene's sequence to the output file
    if gene_name:
        output_f.write(f'>{gene_name}\n{sequence}\n')

print("Duplicate genes extracted and saved to 'duplicate_genes.fa'")