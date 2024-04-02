import re

seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

repetitive_elements = ['GTGTGT', 'GTCTGT']

total_count = 0

for element in repetitive_elements:
    count = len(re.findall(f'(?={element})', seq))
    print(f"The count of '{element}' is: {count}")
    total_count += count

print(f"The total count of repetitive elements is: {total_count}")
