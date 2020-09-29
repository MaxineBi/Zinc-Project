import sys
from getopt import getopt
from Bio.PDB import *
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import os,glob
folder_path = '/databases/mol/pdb/cg'

def read_input2(pdb):
 parser = PDBParser(PERMISSIVE=1, QUIET=True)
 try:
  structure = parser.get_structure("input", pdb)
  return structure
 except OSError as e:
  print('Could not locate PDB file')

for filename in glob.glob(os.path.join(folder_path, '*.ent')):
 with open(filename, 'r') as f:
  FileContents = f.read()
  if FileContents.find('ZINC') != -1 and FileContents.find('X-RAY') != -1:
   print(filename)
   ppb = PPBuilder()
   for pp in ppb.build_peptides(read_input2(filename)):
    print(pp.get_sequence())
   
 SIMONE's CODE:
 def molecular_weight_printer(filename):
 ppb = PPBuilder()
 MW_final = 0
 print(filename[25:29])
 for pp in ppb.build_peptides(structure(filename)):
  seq = pp.get_sequence()
  seqstring = str(seq)
  analysed_seq = ProteinAnalysis(seqstring)
  MW = analysed_seq.molecular_weight()
  MW_final += MW
 print(MW_final)

def sequence_printer(filename):
 ppb = PPBuilder()
 print('>',filename[25:29])
 for pp in ppb.build_peptides(structure(filename)):
  seq = pp.get_sequence()
  seqstring = str(seq)
  print(seqstring)

metalsite =  'BINDING SITE FOR RESIDUE ZN'
metalsitelower = 'binding site for residue ZN'
conditions = 'CRYSTALLIZATION CONDTIONS: ...  ZINC'


for filename in glob.glob(os.path.join(folder_path, '*.ent')):
  with open(filename, 'r') as f:
   FileContents = f.read()
   if FileContents.find(metal) != -1 and FileContents.find(filetype) != -1 and FileContents.find(conditions) != -1:
    molecular_weight_printer(filename)
                                      
