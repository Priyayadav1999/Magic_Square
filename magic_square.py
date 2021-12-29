magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
empty=[]
while i<len(magic_square):
    sum_row=0
    j=0
    while j<len(magic_square[i]):
        sum_row=sum_row+magic_square[i][j]
        j=j+1
    c=0
    sum_column=0
    while c<len(magic_square):
        sum_column=sum_column+magic_square[c][i]
        c=c+1
    if sum_row==sum_column:
        empty=sum_column
    elif sum_row!=sum_column:
        print("this is not magic square")
        break
    i=i+1
    
# for diagonal 1
k=0
sum_dia1=0
while k<len(magic_square):
    sum_dia1=sum_dia1+magic_square[k][k]
    k=k+1
    
# for diagonal 2
b=0
d=len(magic_square)
sum_dia2=0
while b<len(magic_square):
    sum_dia2=sum_dia2+magic_square[b][d-1]
    b=b+1
    d=d-1
if empty==sum_dia1==sum_dia2:
    print("this is a magic square")
