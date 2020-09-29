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
