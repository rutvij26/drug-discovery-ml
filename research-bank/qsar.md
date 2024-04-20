# QSAR ( Quantitative Structure Activity Relationship)


## Molecules

Molecules have Molecule Descritors ( Features )

-   If a feature is present or not in molecule it is denoted as `1` or `0`
-   Molecule is encoded in sequence of 1s and 0s ( binary representation )

## Sample Data set

| x1 | x2 | x3 | x4 | x6 | x7 | x8 | x9 | x10 | x11 | x12 | x13 | x14 | x15 | x16 | __Y__ |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |


-   Each feature is representated from `__( x1 - 16 )__`
-   `Y` represents the biological activity that we want to predict 


## Machine Learning Model

-   We train the machine learning model on the above data to represent __predict__ the biological activity (`Y`) of each molecule
-   We can also use the model to predict the feature importance for the specified biological activity (`Y`)