# 스택, 큐
# 기능개발
import math
# case 1
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
# case 2
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# case 3
# progresses = [96,94]
# speeds = [3,3]
def solution(progresses, speeds):
    ans = []
    job = [-1]
    for i in range(len(progresses)):
        num = math.ceil((100-progresses[i])/speeds[i])
        if(job[-1] > num):
          job.append(job[-1])
        else:
          job.append(num)
    job.remove(-1)
    # print(job)


    for i in range(len(job)-1):
      if i == 0:
        ans.append(1)   
      if job[i] != job[i+1]:
        ans.append(1)
        #ans.append(cnt)
      else:
        ans.append(ans.pop(-1) + 1)

    return ans


# solution(progresses, speeds)

