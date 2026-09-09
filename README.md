# 🧬 NCBI FASTA Sequence Parser

> A practical bioinformatics project for extracting meaningful DNA sequence statistics from real NCBI data using Python and Biopython.

## 🔎 About the Project

Biological databases contain enormous amounts of sequence information. Before performing advanced analysis, researchers often need to obtain basic characteristics of a sequence.

This project demonstrates a simple computational workflow:

**NCBI → FASTA → Biopython → Sequence Analysis → Results**

A DNA sequence downloaded from the **NCBI Nucleotide Database** is used as the input. The Python program parses the FASTA file and reports essential sequence statistics.

---

## 🎯 Project Objective

The objective of this project is to build a Python-based FASTA parser capable of extracting:

- 🆔 Sequence ID
- 📏 Sequence length
- 🧬 GC content

The project combines biological data with programming to demonstrate a fundamental bioinformatics workflow.

---

## 🔬 Analysis Performed

1. FASTA Parsing:
   
The FASTA file is parsed using Biopython's SeqIO module.

3. Sequence Identification:

The program extracts the identifier from the FASTA record.

5. Sequence Length:

The total number of nucleotides is calculated in base pairs (bp).

7. GC Content:
   
The percentage of guanine (G) and cytosine (C) nucleotides is calculated using:

GC Content (%) = (G + C) / Total nucleotides × 100

## 🗃️ Data Source

The input sequence was obtained from the:

**National Center for Biotechnology Information (NCBI)**

NCBI Nucleotide Database:

https://www.ncbi.nlm.nih.gov/nuccore/

The sequence was downloaded in **FASTA format** and saved locally as sequence.fasta

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python** | Programming language |
| **Biopython** | Biological sequence parsing |
| **NCBI** | Biological sequence data source |
| **VS Code** | Development environment |
| **Git** | Version control |
| **GitHub** | Project hosting |

---

## 👤 Author

Fanny R

Bioinformatics Intern

Focused on biological sequence analysis and Python-based bioinformatics workflows.
