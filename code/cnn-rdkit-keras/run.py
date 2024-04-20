import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Reshape

# Generate a random molecule
mol = Chem.MolFromSmiles('Cc1ccccc1')

# Generate a set of candidate molecules using a CNN
model = Sequential()
model.add(Conv1D(32, kernel_size=3, activation='relu', input_shape=(100, 1)))
model.add(MaxPooling1D(pool_size=2))
model.add(Conv1D(64, kernel_size=3, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(128, activation='relu', input_shape=(1472,))) # Specify the input shape here
model.add(Dense(1, activation='sigmoid'))
model.add(Reshape((-1, 1)))
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(np.random.rand(1000, 100, 1), np.random.rand(1000, 1), epochs=10, batch_size=32)
candidates = model.predict(np.random.rand(1, 100, 1))

# Visualize the candidate molecules
# mols = [
#         Chem.MolFromSmiles(
#             Chem.MolToSmiles(
#                 Chem.MolFromSmiles(
#                 	candidate.squeeze()
# 				)
#             )
# 		)
#     for candidate in candidates
# ]

# Convert the numerical values to SMILES strings

mols = [Chem.MolFromSmiles(Chem.MolToSmiles(AllChem.ReplaceSubstructs(mol, Chem.MolFromSmiles('C1CCC1'), candidate))) for candidate in candidates]
img = Draw.MolsToGridImage(mols, molsPerRow=5)
img.show()

# smiles_candidates = [Chem.MolToSmiles(candidate.squeeze()) for candidate in candidates]

# # Remove any invalid SMILES strings and create RDKit molecule objects
# mols = [Chem.MolFromSmiles(smiles) for smiles in smiles_candidates if Chem.MolFromSmiles(smiles) is not None]

# # Visualize the candidate molecules
# img = None
# if mols:
#     img = Draw.MolsToGridImage(mols, molsPerRow=5)
#     img.show()
# else:
#     print("No valid molecules to visualize.")
