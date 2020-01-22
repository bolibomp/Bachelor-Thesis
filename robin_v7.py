from math import *
from pylab import *
initbox=1
axis=2

alpha=1
delta=0.01

epsilon=alpha*delta**2
mu=(1+epsilon)

#def fa(a,mu):
#
#    return (2*mu*a)/((mu-1)*a**2+1)
#
#def StandardMap(delta,q,p,mu):
#    q_next = fa(q+(delta*p/2),mu)/2 + (delta*p/2)
#    p_next = fa(q+(delta*p/2),mu)/delta - (2*q/delta)   
#    return  q_next,p_next
#
#def StandardMapIterate(N, n_init, box):
#    qlen = box[1]-box[0]
#    plen = box[3]-box[2]
#    inits=[]
#    for i in range(n_init):
#        qtemp = (1.1*random()-random())
#        ptemp = (1.1*random()-random())
#        inits.append([qtemp,ptemp])
#    
#    for nums in inits:
#        q=[nums[0]]
#        p=[nums[1]]       
#        for n in range(0,N):
#            qtemp, ptemp = StandardMap(delta,q[n],p[n],mu)
#            q.append( qtemp )            
#            p.append( ptemp )           
#        plot(q,p,',')
#    xlabel('q')
#    ylabel('p')
#    #title('$\alpha= $' + str(alpha))
#    xlim(-axis,axis)
#    ylim(-axis,axis)
#    #gca().set_aspect('equal', adjustable='box')
#    grid()
#    #draw()
#    show()
#StandardMapIterate(N=1000, n_init=500, box = [-1/2*initbox,1/2*initbox,-1/2*initbox,1/2*initbox])

def ApproxStandardMap(delta,q,p,mu):
    q_next = q+delta*p
    p_next = p+2*alpha*delta*(q-(q)**3)  
    return  q_next,p_next

def ApproxStandardMapIterate(N, n_init, box):
    inits=[]
    for i in range(n_init):
        qtemp = (1.1*random()-random())
        ptemp = (1.1*random()-random())
        inits.append([qtemp,ptemp])
    
    for nums in inits:
        q=[nums[0]]
        p=[nums[1]]       
        for n in range(0,N):
            qtemp, ptemp = ApproxStandardMap(delta,q[n],p[n],mu)
            q.append( qtemp )            
            p.append( ptemp )           
        plot(q,p,',')
    xlabel('q')
    ylabel('p')
    #title()
    xlim(-axis,axis)
    ylim(-axis,axis)
    #gca().set_aspect('equal', adjustable='box')
    grid()
    draw()
    #savefig('/Users/Robin/Desktop/Plot/pq.pdf')
    show()
ApproxStandardMapIterate(N=6000, n_init=200, box = [-1/2*initbox,1/2*initbox,-1/2*initbox,1/2*initbox])