magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2] ]
i=0
empty=0
while i<len(magic_square):
    # for row and column
    sum_row=0
    sum_column=0
    j=0
    while j<len(magic_square[i]):
        sum_row=sum_row+magic_square[i][j]
        sum_column=sum_column+magic_square[j][i]
        j=j+1
        # print("sum_row",sum_row,"sum_column",sum_column)
    if sum_row==sum_column:
        empty=sum_column
    elif sum_row!=sum_column:
        print("this is not magic square")
        break
    i=i+1
    
# for diagonal 1 & diagonal 2
k=0
sum_dia1=0
sum_dia2=0
while k<len(magic_square):
    sum_dia1=sum_dia1+magic_square[k][k]
    sum_dia2=sum_dia2+magic_square[k][-k-1]
    k=k+1
if empty==sum_dia1==sum_dia2:
    print("this is a magic square")
else:
    print("this is not magic square")
