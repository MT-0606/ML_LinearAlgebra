# THE GRAM-SCHMIDT PROCESS
# - Used to transform any basis to an orthogonal basis
# - Orthogonalise the second column relative to the first column
# - Do the same to the third column relative to the first two columns
# - Subtract off two parts: one part of the column parallel to the second
#   column and another part relative to the first column
# - Repeat until the last column
# - The result: a matrix in which every column is orthogonal, but the 
#   resultant matrix is not orthogonal
# - Normalise each column. Then we will get an orthogonal matrix.