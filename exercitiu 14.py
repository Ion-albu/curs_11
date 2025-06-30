
# Exercițiul 14: Problema tripletelor
# Condiția: Dat fiind un array de numere întregi nums,
# returnează numărul de triplete (i,j,k) unde i < j < k și
# nums[i] + nums[j] + nums[k] = 0.

nums_triplete = [-1, 0, 1, 2, -1, -4, 0, 3, -2]

# Scrie codul pentru găsirea tripletelor cu suma 0
n = len(nums_triplete)
numar_triplete = 0
for i in range(n):
    for j in range(i + 1,n):
        for k in range(j + 1,n):
            if nums_triplete[i] + nums_triplete[j] + nums_triplete[k] == 0:
                numar_triplete += 1
print(numar_triplete)
