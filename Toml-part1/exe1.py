from asyncio.windows_events import INFINITE
from classes import Inequality
from classes import Equality
from classes import Problem
import math

starts=list()
starts+=[(0,0),(10,20),(-10,1),(-30,-30)]

def e(x):
    if(x[0]<=50):
        return math.exp(x[0])
    else: print("Overlimit")
    return INFINITE;

poly=lambda x:4*(x[0]**2)+2*(x[1]**2)+x[0]*x[1]+2*x[1]+1

fzero=lambda x: e(x)*poly(x)

print("The function fzero is convex because e^x is convex and the quadratic function too")

ineq1=Inequality(lambda x:-x[0]*x[1]+x[0]+x[1]-1.5)
ineq2=Inequality(lambda x:+x[0]*x[1]+10)

p=Problem(fzero,-1)
p.addIneq(ineq1)
p.addIneq(ineq2)

results=[]
for x0 in starts:
    print("Use "+str(x0)+":\n")
    results+=[p.solve(x0,"SLSQP")]

for i in results:
    print("results for "+ str(i.point)+" : ")
    print("     pstar:"+ str(i.value.fun))
    print("     xstar:"+str(i.value.x))
      
def jacobian(x):
    dx0=math.exp(x[0])*(4*x[0]**2+2*x[1]**2+4*x[0]*x[1]+2*x[1]+12*x[0]+1)
    dx1=math.exp(x[0])*(4*x[1]+4*x[0]+2)
    return  [dx0,dx1]

def hessian(x):
    dxx=math.exp(x[0])*(4*x[0]**2+2*x[1]**2+4*x[0]*x[1]+24*x[0]+13)
    dxy=math.exp(x[0])*(4*x[1]+4*x[0]+2)
    dyx=math.exp(x[0])(4*x[1]+4*x[0]+6)
    dyy=math.exp(x[0])*4
    return [[dxx,dyx],[dxy,dyy]]

results=[]

for x0 in starts:
    print("Use "+str(x0)+":\n")
    results+=[p.solveWithJacob(x0,"SLSQP",jacobian)]


for i in results:
    print("results for "+ str(i.point)+" : ")
    print("     pstar:"+ str(i.value.fun))
    print("     xstar:"+str(i.value.x))


results=[]

for x0 in starts:
    print("Use "+str(x0)+":\n")
    results+=[p.solveWithJacobHess(x0,jacobian,hessian)]


for i in results:
    print("results for "+ str(i.point)+" : ")
    print("     pstar:"+ str(i.value.fun))
    print("     xstar:"+str(i.value.x))