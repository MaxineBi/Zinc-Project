import sys
import numpy as np
from Bio.PDB import *
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from sys import argv
import os,glob
folder_path = '/databases/mol/pdb/*/‘
#use path above to direct to where your files are

script, metal, filetype = argv

#call structure from file
def structure(pdb):
 parser = PDBParser(PERMISSIVE=1, QUIET=True)
 try:
  structure = parser.get_structure("input", pdb)
  return structure
 except OSError as e:
  print('Could not locate PDB file')

#return sequence of all chains and pdb identifier
def sequence(filename):
 ppb = PPBuilder()
 return(‘>’,filename[25:29])
 for pp in ppb.build_peptides(structure(filename)):
  seq = pp.get_sequence()
  seqstring = str(seq)
  return(seqstring)


for filename in glob.glob(os.path.join(folder_path, '*.ent')):
  with open(filename, 'r') as f:
   FileContents = f.read()
   if FileContents.find(metal) != -1 and FileContents.find(filetype) != -1:
     print(sequencefilename))
