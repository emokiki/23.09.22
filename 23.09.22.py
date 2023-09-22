""" def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func) """


""" def prt_func() :
    print("hello0")
    print("hello1")
    print("hello2")
    print("hello3")
    print("hello4")

def callfunc(fx) :
		fx()

callfunc(prt_func) """


""" def update_msg(name : str) -> list:
    msg = []
    msg.append("hello, " + name)
    msg.append("Bye, " + name)
    return msg

def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg  """



""" def prt_func(n) :
    print("hello", n)

    def callfunc(x) :

 """


""" def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    #print(2, n)
    
fun(1) """

#factorial

""" def ploop(n) :
    if n == 0:
        print("end")
        return 1
    else :
        print(n, n-1, "=", n + n-1)
        return n * ploop(n-1)
    
print(ploop(3)) """

""" def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res = ", res) """

""" 
import calc

print(dir (calc)) """


""" import calc
add_res = calc.add(1,2)
sub_res = calc.sub(1,2)
mul_res = calc.mul(1,2)
div_res = calc.div(1,2) """


""" import calc as c1
add_res = c1.add(3,6)
sub_res = c1.sub(3,6)
mul_res = c1.mul(3,6)
div_res = c1.div(3,6) """


# import mod.circle_mod as cm

# print(cm.pi)
# print(cm.cc_area(4))
# print(cm.cc_len(5))


""" def cutstr(st, wd, idx) :
    tmp = st.split(wd)
    res = tmp(idx)
    return res
 """
""" url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
rs = cutstr(url, "/", 3)
print(rs) """



# import math

# sq_res = math.sqrt(6)
# print(sq_res)

# sq_res=math.sin(math.pi / 2)
# print(sq_res)

# e_res = math.log(math.e)
# print(e_res)

# exp_res = math.exp(3)
# print(exp_res)

# pi_res = math.pi
# print(pi_res)

# fc_res = math.factorial(4)
# print(fc_res)



# import mod.utils as mu

# res= mu.mt_sqrt(7)
# print(res)

# sin = mu.mt_sinpi()
# print(sin)

# el = mu.mt_elog()
# print(el)

# ep = mu.mt_exp(3)
# print(ep)

# pi=mu.mt_pi()
# print(pi)


""" import random as rd

res = rd.randint(1,100)
print(res)

my_list = ["apple" , "banana" , "cherry"]
Lres = rd.choice(my_list)
print(Lres)

fres = rd.random()
print(fres)


nvres = rd.normalvariate()
print(nvres)
 """

