from Bio import SeqIO


def calculate_gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    sequence = str(sequence).upper()

    if len(sequence) == 0:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def parse_fasta(filename):
    """Parse an NCBI FASTA file and display sequence information."""

    for record in SeqIO.parse(filename, "fasta"):
        sequence_id = record.id
        sequence_length = len(record.seq)
        gc_content = calculate_gc_content(record.seq)

        print(f"Sequence ID: {sequence_id}")
        print(f"Length: {sequence_length} bp")
        print(f"GC Content: {gc_content:.2f}%")
        print("-" * 40)


if __name__ == "__main__":
    # FASTA sequence downloaded from NCBI
    fasta_file = "sequence.fasta"

    parse_fasta(fasta_file)