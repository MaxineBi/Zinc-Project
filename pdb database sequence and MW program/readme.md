This program takes 3 arguments:

python script(either PDBsequencereader.py or MolecularWeightofPDB.py) searchword1 searchword2

In this case, search word 1 was a metal (ZN) which is why it was annotated as such. We used '  ZN  ' to make sure it was found in the structure.
"ZINC" or "ZN" was sometimes found in other places in the file, but in atom identifiers it always had the spacing around it.

Searchword2 in this case was the method used, 'X-RAY DIFFRACTION' or 'NMR'.

These terms can be substituted for any searchwords.

Within the files, one can change the file path, or change what the functions return (to print the filename/PDB identifier or just sequence or MW).

These work by first creating a structure object from the file with Biopython.
Then, from the structure object, a sequence object is also created with Biopython. This object is translated in a string, and all strings (corresponding to all chains in the atom) are returned for each pdb file.

Then, to calculate the molecular weight from each structure, each chain is converted into a MW using Protein analysis from Bio.SeqUtils.ProtParam (also biopython)
And the MW of all chains are cocatenated to a final molecular weight.

The 'find' function is used to iterate through all files with the two search words (in this case, metal and filetype), and run the functions on them.
