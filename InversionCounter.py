

def SortList(num_list):
   l = len(num_list)
   if l > 1:
      n = l//2
      list_1 = num_list[:n]
      list_2 = num_list[n:]
      list_1, list_1_ic = SortList(num_list[:n])
      list_2, list_2_ic = SortList(num_list[n:])
      B, b = MergeList(C,D)
      return B, b+c+d
   else:
      return A, 0


def MergeList(A,B):
   count = 0
   M = []
   while A and B:
      if A[0] <= B[0]:
         M.append(A.pop(0))
      else:
         count += len(A)
         M.append(B.pop(0))
   M  += A + B
   return M, count

with open('data.txt') as f:
    list_num = []
    for line in f:
        if line:
            list_num.append(int(line))
print 'Inverstion Count for data from data.txt: ' + str(SortCount(list_num)[1])
