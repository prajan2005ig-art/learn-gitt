mat = [[1,2,3],[12,3,4],[0,3,4]]
target = 3
found = False
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == target:
            print("found at row : ", i,"column : ", j)
            found = True
            break

if found == False:
    print("not found")
