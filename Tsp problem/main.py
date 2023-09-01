import random as r
import numpy as np
import matplotlib.pyplot as plt


def make_perm(n):
    try:
        lst=list()
        while(len(lst)<n):
            j=r.randint(0,n-1)
            if  bool(j in lst)==False:
                lst.append(j)
        return lst
    except:
        print("n is wrong number >>> _ make_perm(n)")


        

        
        
def crossover_perm_2p(par1,par2):
    n=len(par1)
    child=[]
    for i in range(n):
        child.append("null")
    p1=r.randint(0,int(0.25*n))
    p2=r.randint(int(0.5*n),int(0.8*n))
    for s in range(0,p1+1):
        child[s]=par1[s]
        
    for t in range(p2+1,n):
        child[t]=par1[t]
        
    for j in range(p1+1,p2+1):
        if bool(par2[j] in child)== False:
            child[j]=par2[j]
        else:
            for w in range(n):
                if bool(par2[w] in child) ==False :
                    child[j]=par2[w]
                    break

    return child
        
        
        
        
        
        

    
def make_bin(n):
    try:
            lst=list()
            for i in range(n):
                lst.append(r.randint(0,1))
            return lst
    except:
        print("n is wrong number >>> _ make_bin()")
        

        
        
        
        
def make_random_array_1_100(n):
    try:
            lst=list()
            for i in range(n):
                lst.append(r.randint(1,100))
            return lst
    except:
        print("n is wrong number >>>_make_random_array_1_100(n)")
        
        
        
        

        
def init_tsp():
    
            global dis; global n_tsp ; global sol_tsp ;
            n_tsp=r.randint(20,200)
            sol_tsp=make_perm(n_tsp)
            dis=np.zeros((n_tsp,n_tsp),dtype=int)
            for i in range(n_tsp):
                for j in range(n_tsp):
                    if i==j:
                        dis[i][j]=0
                    else:
                        val=r.randint(5,100)
                        dis[i][j]=val
                        dis[j][i]=val
                        
                        
                        
                        
def eval_tsp(arr):
    try:
            path_cost=0
            for i in range(len(arr)):
                if i==(len(arr)-1):
                    path_cost+=dis[arr[len(arr)-1]][arr[0]]
                else:
                    path_cost+=dis[arr[i]][arr[i+1]]
                    
            return path_cost
                
        
    except:
            print("error >>>>>>  eval_tsp(arr)")

            
            
            

def selection(eval_pop, n_pop, k=3, eval_type=1):
    
        selection_l = list()
        for p in range(2):
            i_minmax = r.randint(0, len(eval_pop) - 1)
            index_list = list()
            while (len(index_list)<k-1):
                index = r.randint(0, len(eval_pop) - 1)
                if (bool(index in index_list ) == False) and (index != i_minmax):
                    index_list.append(index)
            for i in index_list:
                if eval_type == 1 and eval_pop[i] > eval_pop[i_minmax]:
                    i_minmax = i
                if eval_type == -1 and eval_pop[i] < eval_pop[i_minmax]:
                    i_minmax = i
    
            selection_l.append(i_minmax)
            
        return pop[selection_l[0]],pop[selection_l[1]]
    
    
    
    
    


    
def crossover_perm_uni(par1,par2):
    n=len(par1)
    mask=make_bin(n)
    child=[]
    for ind in range(n):
        child.append("null")
        
    for i in range(n):
        if mask[i]==1:
            child[i]=par1[i]
    for j in range(n):
        if mask[j]==0 and bool(par2[j] in child)==False:
            child[j]= par2[j]
        elif mask[j]==0 and bool(par2[j] in child)==True:
            for t in range(n):
                if bool(par2[t] in child)==False :
                    child[j]=par2[t]
                    break
    
    return child






def tweak_perm(arr):
    n=len(arr)
    ind1=r.randint(0,n-1)
    ind2=r.randint(0,n-1)
    ind3=r.randint(0,n-1)
    ind4=r.randint(0,n-1)
    arr[ind1],arr[ind2]=arr[ind2],arr[ind1]
    arr[ind3],arr[ind4]=arr[ind4],arr[ind3]
    tweak_arr=arr
    
    return tweak_arr




def min_chr(arr):
    minim=arr[0]
    index=0
    for i in range(1,len(arr)):
        if arr[i]<minim:
            minim=arr[i]
            index=i
    return index





def choose_elite(ar_p, ar_e, c=1):
    for i in range(c):
        best_ind = min_chr(ar_e)
        best_chr.append(ar_p[best_ind])
        best_eval.append(ar_e[best_ind])
        ar_p.pop(best_ind)
        ar_e.pop(best_ind)
        
        
        


# Genetic algorithm


# Primary population production

init_tsp()
n_pop = r.randint(50, 300)
n_iter = r.randint(50, 500)
pop = list()
eval_pop = list()
best_chr = list()
best_eval = list()

for i in range(n_pop):
    ch = make_perm(n_tsp)
    pop.append(ch)
    eval_pop.append(eval_tsp(ch))

#elitism

e_c =r.randint(1,8)
choose_elite(pop, eval_pop, c=e_c)

# iteration phase

bsp=list()
bs_ch=list()
for itere in range(0, n_iter ):
    new_pop = list()
    new_eval_pop = list()
    new_pop = new_pop + best_chr
    new_eval_pop = new_eval_pop + best_eval 
    k_=r.randint(3,8)
    for ch in range(e_c, n_pop):
        parent1, parent2 = selection(eval_pop=eval_pop, n_pop=n_pop, k=k_, eval_type=-1)
        flag=r.randint(0,1)
        if flag==0:
            cr = crossover_perm_uni(parent1, parent2)
            new_pop.append(cr)
        if flag==1:
            cr=crossover_perm_2p(parent1,parent2)
            new_pop.append(cr)
        
        mutation_prob = r.random()
        if (mutation_prob < 0.3):
            new_pop[ch] = tweak_perm(new_pop[ch])
            
        new_eval_pop.append(eval_tsp(new_pop[ch]))

    pop = new_pop
    eval_pop = new_eval_pop
    choose_elite(pop, eval_pop, c=e_c)
    b_index=min_chr(best_eval)
    bsp.append(best_eval[b_index])
    bs_ch.append(best_chr[b_index])
    best_chr = best_chr[e_c:2 * e_c]
    best_eval = best_eval[e_c:2 * e_c]
    


b_index=min_chr(bsp)
print("BEST SOLUTION FOR TSP PROBLEM IS :  \n")
print(bs_ch[b_index])
print("Total path cost  : ", bsp[b_index])
print("iteration >> ",b_index)
print("elitism factor",e_c)
plt.plot( range(n_iter),bsp)
plt.title("TSP problem  >>>> Genetic Algorithm")
plt.xlabel("iteration")
plt.ylabel(" Best path cost")
plt.show()

