class SequenceComparer:
    def __init__(self, blosum62_file_path, fasta_files_paths):
        self.blosum62 = self.read_blosum62(blosum62_file_path)
        self.sequences = {name: self.read_fasta_file(file_path) for name, file_path in fasta_files_paths.items()}

    def read_fasta_file(self, file_path):
        with open(file_path, 'r') as file:
            sequence = ""
            for line in file:
                if line[0] != '>':
                    sequence += line.strip()
            return sequence

    def read_blosum62(self, file_path):
        with open(file_path, 'r') as file:
            blosum62 = {}
            next(file)

            for i, line in enumerate(file, 1):
                parts = line.split()
                amino_acid_1 = parts[0]
                scores = list(map(int, parts[1:])) 
            
                for col_num, score in enumerate(scores, start=1):
                    amino_acid_2 = parts[col_num-1]
                    blosum62[(amino_acid_1, amino_acid_2)] = score
                    blosum62[(amino_acid_2, amino_acid_1)] = score
                           
        return blosum62

    def calculate_score(self, seq1, seq2):
        score = 0
        for aa1, aa2 in zip(seq1, seq2):
            score += self.blosum62.get((aa1, aa2), 0) 
        return score

    def calculate_identity(self, seq1, seq2):
        return sum(aa1 == aa2 for aa1, aa2 in zip(seq1, seq2))

    def compare_sequences(self, name1, name2):
        seq1 = self.sequences.get(name1)
        seq2 = self.sequences.get(name2)

        if seq1 is None or seq2 is None:
            print("Error: One or both sequences not found.")
            return

        score = self.calculate_score(seq1, seq2)
        identity = self.calculate_identity(seq1, seq2)

        print(f"{name1} vs {name2}: Score = {score}, Identity = {identity / len(seq1) * 100:.2f}%")
        return score

    def find_best_model_organism(self):
        human_mouse_score = self.compare_sequences("SLC6A4_HUMAN", "SLC6A4_MOUSE")
        human_rat_score = self.compare_sequences("SLC6A4_HUMAN", "SLC6A4_RAT")

        if human_mouse_score > human_rat_score:
            print("The mouse sequence is more closely related to the human sequence.")
            print("The mouse is a better model organism for human based on the SLC6A4 gene sequence.")
        else:
            print("The rat sequence is more closely related to the human sequence.")
            print("The rat is a better model organism for human based on the SLC6A4 gene sequence.")


# Usage example:
blosum62_file_path = "C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/BLOSUM62.txt"  # Provide the path to your BLOSUM62 file
fasta_files_paths = {
    "SLC6A4_HUMAN": "C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/SLC6A4_HUMAN.fa",
    "SLC6A4_MOUSE": "C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/SLC6A4_MOUSE.fa",
    "SLC6A4_RAT": "C:/Users/17732/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 13/SLC6A4_RAT.fa"
}

sequence_comparer = SequenceComparer(blosum62_file_path, fasta_files_paths)
sequence_comparer.find_best_model_organism()
