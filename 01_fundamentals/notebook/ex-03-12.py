def average(x,y,z):
    rSum = 0
    rSum =  x+y+z
    rAve = rSum/3
    return rAve

def middle_number(x,y,z):
    rList = []
    rList.append(x)
    rList.append(y)
    rList.append(z)
    rList.sort()
    return rList[1]

def str_odd(x):
    if x % 2 == 1:
        return 'odd'
    else:
        return 'even'

def number_info(strn):
    nums = strn.split(' ')
    x = int(nums[0])
    y = int(nums[1])
    z = int(nums[2])

    num_ave = average(x,y,z)
    mid_num = middle_number(x,y,z)
    odd = str_odd(mid_num)
    return 'The average of the three numbers: ' + str(num_ave) +'\n' + 'Middle number: '+ str(mid_num) + '\nIt is ' + odd
   
    