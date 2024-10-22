import operator
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x:(x[col-1],-x[0]))
    #print(data)
    for i in range(row_begin,row_end+1):
        cur_row = data[i-1]  
        temp = sum(r%i for r in cur_row)  
        answer = operator.xor(answer, temp)
    #print(operator.xor(0, 4))
    return answer