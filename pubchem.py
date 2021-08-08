import pubchempy as pcp
Chem = pcp.get_compounds("CC",'smiles')

Inform= pcp.compounds_to_frame(Chem, properties=['xlogp','synonyms'])
print(list(Inform['synonyms'])[0][0],cids)