# Comparing `tmp/proteinTools-0.1.2.tar.gz` & `tmp/proteinTools-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "proteinTools-0.1.2.tar", last modified: Thu Apr  6 18:23:18 2023, max compression
+gzip compressed data, was "proteinTools-0.1.3.tar", last modified: Thu Apr  6 23:12:26 2023, max compression
```

## Comparing `proteinTools-0.1.2.tar` & `proteinTools-0.1.3.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwx---   0 defrondeville.c (1825595208) users      (100)        0 2023-04-06 18:23:18.311504 proteinTools-0.1.2/
--rw-rw----   0 defrondeville.c (1825595208) users      (100)     1069 2023-04-05 17:13:20.000000 proteinTools-0.1.2/LICENSE
--rw-rw----   0 defrondeville.c (1825595208) users      (100)      451 2023-04-06 18:23:18.304135 proteinTools-0.1.2/PKG-INFO
--rw-rw----   0 defrondeville.c (1825595208) users      (100)      269 2023-04-06 05:13:03.000000 proteinTools-0.1.2/README.md
-drwxrwx---   0 defrondeville.c (1825595208) users      (100)        0 2023-04-06 18:23:18.192117 proteinTools-0.1.2/proteinTools/
--rw-rw----   0 defrondeville.c (1825595208) users      (100)       33 2023-04-06 18:18:10.000000 proteinTools-0.1.2/proteinTools/__init__.py
--rw-rw----   0 defrondeville.c (1825595208) users      (100)    28430 2023-04-06 18:22:21.000000 proteinTools-0.1.2/proteinTools/proteinTools.py
-drwxrwx---   0 defrondeville.c (1825595208) users      (100)        0 2023-04-06 18:23:18.263001 proteinTools-0.1.2/proteinTools.egg-info/
--rw-rw----   0 defrondeville.c (1825595208) users      (100)      451 2023-04-06 18:23:18.000000 proteinTools-0.1.2/proteinTools.egg-info/PKG-INFO
--rw-rw----   0 defrondeville.c (1825595208) users      (100)      224 2023-04-06 18:23:18.000000 proteinTools-0.1.2/proteinTools.egg-info/SOURCES.txt
--rw-rw----   0 defrondeville.c (1825595208) users      (100)        1 2023-04-06 18:23:18.000000 proteinTools-0.1.2/proteinTools.egg-info/dependency_links.txt
--rw-rw----   0 defrondeville.c (1825595208) users      (100)       13 2023-04-06 18:23:18.000000 proteinTools-0.1.2/proteinTools.egg-info/top_level.txt
--rw-rw----   0 defrondeville.c (1825595208) users      (100)       38 2023-04-06 18:23:18.326896 proteinTools-0.1.2/setup.cfg
--rw-rw----   0 defrondeville.c (1825595208) users      (100)      429 2023-04-06 18:22:30.000000 proteinTools-0.1.2/setup.py
+drwxrwx---   0 defrondeville.c (1825595208) users      (100)        0 2023-04-06 23:12:26.942133 proteinTools-0.1.3/
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)     1069 2023-04-05 17:13:20.000000 proteinTools-0.1.3/LICENSE
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)      451 2023-04-06 23:12:26.938363 proteinTools-0.1.3/PKG-INFO
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)      269 2023-04-06 05:13:03.000000 proteinTools-0.1.3/README.md
+drwxrwx---   0 defrondeville.c (1825595208) users      (100)        0 2023-04-06 23:12:26.855200 proteinTools-0.1.3/proteinTools/
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)       33 2023-04-06 18:18:10.000000 proteinTools-0.1.3/proteinTools/__init__.py
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)    33577 2023-04-06 23:11:49.000000 proteinTools-0.1.3/proteinTools/proteinTools.py
+drwxrwx---   0 defrondeville.c (1825595208) users      (100)        0 2023-04-06 23:12:26.920266 proteinTools-0.1.3/proteinTools.egg-info/
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)      451 2023-04-06 23:12:26.000000 proteinTools-0.1.3/proteinTools.egg-info/PKG-INFO
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)      224 2023-04-06 23:12:26.000000 proteinTools-0.1.3/proteinTools.egg-info/SOURCES.txt
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)        1 2023-04-06 23:12:26.000000 proteinTools-0.1.3/proteinTools.egg-info/dependency_links.txt
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)       13 2023-04-06 23:12:26.000000 proteinTools-0.1.3/proteinTools.egg-info/top_level.txt
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)       38 2023-04-06 23:12:26.948470 proteinTools-0.1.3/setup.cfg
+-rw-rw----   0 defrondeville.c (1825595208) users      (100)      429 2023-04-06 22:47:07.000000 proteinTools-0.1.3/setup.py
```

### Comparing `proteinTools-0.1.2/LICENSE` & `proteinTools-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `proteinTools-0.1.2/proteinTools/proteinTools.py` & `proteinTools-0.1.3/proteinTools/proteinTools.py`

 * *Files 8% similar despite different names*

```diff
@@ -16,15 +16,14 @@
 mg = mygene.MyGeneInfo()
 
 #Utility dictionaries containing element/mass mappings as well as FASTA mapping
 FASTAdict = {'ALA':'A', 'ALX':'B', 'CYS': 'C', 'ASP' : 'D', 'GLU': 'E', 'PHE': 'F', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LYS':'K', 'LEU':'L', 'MET': 'M', 'ASN':'N', 'PRO':'P', 'GLN': 'Q', 'ARG':'R', 'SER': 'S', 'THR': 'T', 'VAL': 'V', 'TRP': 'W', 'UNK':'X', 'TYR':'Y', 'GLX':'Z'}
 atom_dict = {'H':1.01, 'C':12.01, 'O':16.00, 'N':14.01, 'P':30.97, 'F':18.998, 'S':32.06, 'B':10.81, 'K':39.1, 'I':126.904, 'BR':79.904, 'CL':35.453, 'CA':40.08, 'NA':22.99, 'MG':24.305, 'AL':26.98, 'CR':51.996, 'NE':20.179, 'BE':9.01, 'FE':55.847, 'CO':58.933,'AG':107.868, 'CD':112.41, 'NI':58.693, 'ZN':65.39, 'BE':9.0122, 'IN':114.818, 'SI':28.085, 'SC':44.956, 'TI':47.867, 'V':50.941, 'MN':54.938, 'CU':63.546, 'GA':59.723, 'GE':72.64, 'SE':78.96, 'KR':83.8, 'ZR':91.224, 'NB':92.906, 'PD':106.42, 'SN':118.71, 'SB':121.76, 'XE':131.293, 'BA':137.327, 'LA':138.91, 'LI':6.941, 'HG':200.59, 'PB':207.2, 'BI':208.98, 'PO':209, 'TI':204.3833, 'AU':196.9665, 'IR':192.217, 'PT':195.078, 'RE':186.207, 'W':183.84, 'TA':180.948, 'YB':173.04, 'EU':151.964, 'ND':144.25, 'CE':140.116, 'TH':232.04, 'U':238.029, 'PU':244, 'FR':223, 'PA':231.04, 'HO':164.93, 'SM':150.36, 'PR':140.908, 'TE':127.6, 'TC':98, 'Y':88.906}
 atom_keys = atom_dict.keys()
 
-
 #Subclass for individual atoms
 class atom:
     def __init__(self, element, x, y, z, data, residue = ''):
         self.element = element
         self.x = x
         self.y = y
         self.z = z
@@ -93,14 +92,15 @@
             y += atom.y
             z += atom.z
             totmass += atom.mass
         x /= totmass
         y /= totmass
         z /= totmass
         return [x, y, z]
+        
 #Main protein class
 class Protein:
     def __init__(self, protein_name, protein_type = 'PDB', species = 'human'):
         self.protein = protein_name
         self.ID_type = protein_type
         self.species = species
         
@@ -449,59 +449,170 @@
                 except:
                     pass
                 if uniprot != None:
                     return uniprot
                 else:
                     raise KeyError
             except:
+                try:
+                    url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
+                    Data = requests.get(url).text
+                    firstResultIndex = Data.index('primaryAccession')
+                    uniprot = Data[firstResultIndex + 19:firstResultIndex + 25] 
+                
+                    return uniprot
+                except Exception as e:
+                    print('Cannot find valid Uniprot ID for protein ' + self.protein + '!')
+                    return 'N/A'
+        elif self.ID_type.upper() == 'HGNC':
+            out = mg.querymany(self.protein, scopes = 'symbol', fields = 'uniprot', species = self.species)
+            try:
+                uniprot = out[0]['uniprot']
+                try:
+                    uniprot = out[0]['uniprot']['Swiss-Prot']
+                except:
+                    pass
+                if uniprot != None:
+                    return uniprot
+                else:
+                    raise KeyError
+            except:
                try:
                    url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
-                   Data = requests.get(line).text
+                   Data = requests.get(url).text
                    firstResultIndex = Data.index('primaryAccession')
                    uniprot = Data[firstResultIndex + 19:firstResultIndex + 25] 
                    return uniprot
                except:
                    print('Cannot find valid Uniprot ID for protein ' + self.protein + '!')
                    return 'N/A'
+        else:
+            try:
+                url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
+                Data = requests.get(url).text
+                firstResultIndex = Data.index('primaryAccession')
+                uniprot = Data[firstResultIndex + 19:firstResultIndex + 25] 
+                return uniprot
+            except:
+                print('Cannot find valid Uniprot ID for protein ' + self.protein + '!')
+                return 'N/A'
     
     #Returns a PDB identifier
     @cached_property 
     def PDB(self):
+        def scrape_data(PDB):  
+            resdf = pd.DataFrame()
+            resolutions, residue_number, lignums, proteins = [], [], [], []
+            for ID in PDB:
+                curr_lig, lignum = '', 0
+                protname = ID + '.pdb'
+                try:
+                    urllib.request.urlretrieve('http://files.rcsb.org/download/' + protname, protname)
+                except:
+                    continue
+                with open(protname, 'r') as f:
+                    data, resolution = f.readlines(), 0
+                for line in data:
+                    if 'RESOLUTION' in line and line[:6] == 'REMARK':  
+                        line = [l for l in line.split(' ') if l != '']
+                        try:
+                            resolution = float(line[3])
+                        except:
+                            break
+                        break
+                resolutions.append(resolution)
+                curr_chain, tot_res = '', 0
+                for count, line in enumerate(data):
+                    if line[0:6] == 'SEQRES':
+                        chain = line[11:12]
+                        if curr_chain != chain:
+                            curr_chain = chain
+                            tot_res += int(line[13:17].strip())
+                
+                    if line[0:6] == 'HETATM':
+                        ligands = line[17:20]
+                        if ligands == 'HOH':
+                            break
+                        if ligands != curr_lig:
+                            curr_lig = ligands
+                            lignum += 1
+                lignums.append(lignum)    
+                residue_number.append(tot_res)
+                os.remove(protname)
+                proteins.append(ID)
+                
+            df = pd.DataFrame.from_dict({'PDB': proteins, 'Resolution':resolutions, 'Residue Number':residue_number, 'Unique Ligands': lignums})
+            df = df[df['Resolution'] > 0]
+            df = df.sort_values(by = 'Resolution', ascending = True, ignore_index = True)
+            return df         
         if self.ID_type == 'PDB': 
-            return self.protein
-        elif self.ID_type.upper() == 'UNIPROT':
-            out = mg.querymany(self.protein, scopes = 'uniprot', fields = 'pdb', species = self.species)
+            return scrape_data([self.protein])
+        elif self.ID_type == 'Uniprot':
             try:
+                out = mg.querymany(self.protein, scopes = 'uniprot', fields = 'pdb', species = self.species)
                 pdb = out[0]['pdb']
-                return pdb
+                return scrape_data(pdb)
             except:
                 try:
-                    url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
-                    Data = requests.get(line).text
-                    firstResultIndex = Data.index('PDB')
-                    pdb = Data[firstResultIndex + 11:firstResultIndex + 15]
-                    return pdb
+                    PDB_IDs, index = [], 0
+                    try:
+                        url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
+                        Data = requests.get(url).text
+                        while True:
+                            firstResultIndex = Data.index('"PDB"')
+                            pdb = Data[firstResultIndex + 12:firstResultIndex + 16]
+                            Data =  Data[firstResultIndex + 20:]
+                            PDB_IDs.append(pdb)
+                    except:
+                        pass
+                    PDB_IDs = list(set(PDB_IDs))
+                    return scrape_data(PDB_IDs)
                 except:
                     print('Cannot find valid PDB ID for protein ' + self.protein + '!')
                     return 'N/A'
-        elif self.ID_type.upper() == 'HGNC':
-            out = mg.querymany(self.protein, scopes = 'uniprot', fields = 'pdb', species = self.species)
+        elif self.ID_type == 'HGNC':
             try:
+                out = mg.querymany(self.protein, scopes = 'symbol', fields = 'pdb', species = self.species)
                 pdb = out[0]['pdb']
-                return pdb
+                return scrape_data(pdb)
             except:
                 try:
-                    url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
-                    Data = requests.get(line).text
-                    firstResultIndex = Data.index('PDB')
-                    pdb = Data[firstResultIndex + 11:firstResultIndex + 15]
-                    return pdb
+                    PDB_IDs, index = [], 0
+                    try:
+                        url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
+                        Data = requests.get(url).text
+                        while True:
+                            firstResultIndex = Data[index:].index('PDB')
+                            pdb = Data[firstResultIndex + 11:firstResultIndex + 15]
+                            PDB_IDs.append(pdb)
+                            index += firstResultIndex + 20
+                    except:
+                        pass
+                    return scrape_data(PDB_IDs)
                 except:
                     print('Cannot find valid PDB ID for protein ' + self.protein + '!')
                     return 'N/A'
+        else:
+            try:
+                PDB_IDs, index = [], 0
+                try:
+                    url = 'https://rest.uniprot.org/uniprotkb/search?query=' + self.protein + '%20' + self.species
+                    Data = requests.get(url).text
+                    while True:
+                        firstResultIndex = Data[index:].index('PDB')
+                        pdb = Data[firstResultIndex + 11:firstResultIndex + 15]
+                        PDB_IDs.append(pdb)
+                        index += firstResultIndex + 20
+                except:
+                    pass
+                return scrape_data(PDB_IDs)
+            except:
+                print('Cannot find valid PDB ID for protein ' + self.protein + '!')
+                return 'N/A'
+        
     
     #Returns HGNC identifier
     @cached_property
     def HGNC(self):
         if self.ID_type == 'HGNC':
             return self.protein
         else:
@@ -602,19 +713,16 @@
             print(traceback.format_exc())
             return 'N/A'
     '''
     TODO
     - Add secondary structure prediction to residues (use s4pred?)
     - Add more ID conversions
     '''
-'''    
+'''
 #For unit testing    
 if __name__ == '__main__':
-    protein = Protein('1HK4')
-    protein.download()
-    print(protein[1])
-    print(protein[1].center)
-    #print(protein.FASTA)
-    new = Protein(protein.Uniprot)
+    p = Protein('1HK4')
+    new = Protein(p.Uniprot)
     new.download()
+    print(new.interactions)
     #print(protein.interactions)
 '''
```

