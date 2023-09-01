# solve  knapsack problem 0_1  with Genetic Algorithm

import random as r
import matplotlib.pyplot as plt

def max_chr(arr):
    maxim = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > maxim:
            maxim = arr[i]
            index = i
    return index


def make_random_array_1_100(n):
    try:
        lst = list()
        for i in range(n):
            lst.append(r.randint(1, 100))
        return lst
    except:
        print("n is wrong number >>>_make_random_array_1_100(n)")


# make binary array for random solution (binary Chromosome)
def make_bin_knapsack(n):
    try:
        while(1):
            lst = list()
            for i in range(n):
                lst.append(r.randint(0, 1))
            if eval_knbsack(lst)>0:
                break
        return lst
    except:
        print("n is wrong number >>> _ make_bin()")

        
        
def make_bin(n):
    try:
            lst=list()
            for i in range(n):
                lst.append(r.randint(0,1))
            return lst
    except:
        print("n is wrong number >>> _ make_bin()")
        
        



# Creation problem variables with random values
def init_knapsck():
    global w_arr;
    global v_arr;
    global n_nbck;
    global w_max;
    n_nbck = r.randint(20, 200)
    w_arr = make_random_array_1_100(n_nbck)
    summ=0
    for we in w_arr:
        summ+=we
    w_max = r.randint(int(0.2*summ),int(0.8*summ))
    v_arr = make_random_array_1_100(n_nbck)


# evaluation knabsack solutions
def eval_knbsack(arr):
    try:
        sum_w = 0
        sum_v = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                sum_v += v_arr[i]
                sum_w += w_arr[i]
        if sum_w <= w_max:
            return sum_v
        else:

            return 0
    except:
        print("error >>>>>>  eval_knbsack(arr)")


# select 2 Chromosome from k Chromosomes
def selection(eval_pop, n_pop, k=3, eval_type=1):
    selection_l = list()
    for p in range(2):
        i_minmax = r.randint(0, len(eval_pop) - 1)
        index_list = list()
        while (len(index_list) < k - 1):
            index = r.randint(0, len(eval_pop) - 1)
            if (bool(index in index_list) == False) and (index != i_minmax):
                index_list.append(index)
        for i in index_list:
            if eval_type == 1 and eval_pop[i] > eval_pop[i_minmax]:
                i_minmax = i
            if eval_type == -1 and eval_pop[i] < eval_pop[i_minmax]:
                i_minmax = i

        selection_l.append(i_minmax)

    return (pop[selection_l[0]], pop[selection_l[1]])


# Two-Point Crossover (binary Chromosome)

def crossover_bin_2p(par1, par2):
    n = n_nbck
    child = [x for x in range(n)]
    p1 = r.randint(0, int(0.25 * n))
    p2 = r.randint(int(0.5 * n), n - 1)
    for i in range(0, p1 + 1):
        child[i] = par1[i]
    for j in range(p1 + 1, p2 + 1):
        child[j] = par2[j]
    for s in range(p2 + 1, n):
        child[s] = par1[s]

    return child


# uniform crossover (binary Chromosome)
def crossover_bin_uni(par1, par2):
    n = n_nbck
    child = make_bin(n)
    mask = make_bin(n)
    for i in range(n):
        if mask[i] == 1:
            child[i] = par1[i]
        elif mask[i] == 0:
            child[i] = par2[i]
    return child


# mutation function (binary Chromosome)
def tweak_bin(arr):
    n = n_nbck
    ind1 = r.randint(0, n - 1)
    ind2 = r.randint(0, n - 1)

    if arr[ind1] == 0:
        arr[ind1] = 1
    else:
        arr[ind1] = 0

    if arr[ind2] == 1:
        arr[ind2] = 0
    else:
        arr[ind2] = 1

    tweak_arr = arr

    return tweak_arr




def choose_elite(ar_p, ar_e, c=1):
    for i in range(c):
        best_ind = max_chr(ar_e)
        best_chr.append(ar_p[best_ind])
        best_eval.append(ar_e[best_ind])
        ar_p.pop(best_ind)
        ar_e.pop(best_ind)
        
        
        



# Genetic algorithm


# Primary population production

init_knapsck()
n_pop = r.randint(100, 200)
n_iter = r.randint(50, 500)
pop = list()
eval_pop = list()
best_chr = list()
best_eval = list()

for i in range(n_pop):
    ch = make_bin_knapsack(n_nbck)
    pop.append(ch)
    eval_pop.append(eval_knbsack(ch))

# elitism
e_c =r.randint(1,8)
choose_elite(pop, eval_pop, c=e_c)

# iteration phase

bp_e=list()
bp_ch=list()
for itere in range(0, n_iter ):
    new_pop = list()
    new_eval_pop =list() 
    new_pop = new_pop + best_chr
    new_eval_pop = new_eval_pop + best_eval
    k_=r.randint(3,8)
    for ch in range(e_c, n_pop):
        parent1, parent2 = selection(eval_pop=eval_pop, n_pop=n_pop, k=3, eval_type=1)
        flag=r.randint(0,1)
        if flag==0:
            cr = crossover_bin_uni(parent1, parent2)
            new_pop.append(cr)
            
        if flag==1:
            cr=crossover_bin_2p(parent1,parent2)
            new_pop.append(cr)

        mutation_prob = r.random()
        if (mutation_prob <= 0.3):
            new_pop[ch] = tweak_bin(new_pop[ch])
            
        new_eval_pop.append(eval_knbsack(new_pop[ch]))

    pop = new_pop
    eval_pop = new_eval_pop
    choose_elite(pop, eval_pop, c=e_c)
    b_index=max_chr(best_eval)
    bp_e.append(best_eval[b_index])
    bp_ch.append(best_chr[b_index])
    best_chr = best_chr[e_c:2 * e_c]
    best_eval = best_eval[e_c:2 * e_c]
    



    
b_index=max_chr(bp_e)
print("BEST SOLUTION FOR KNAPSACK PROBLEM IS :  \n")
print(bp_ch[b_index])
print("PROFIT \n: ", bp_e[b_index])
print("iteration >> ",b_index)
print("elitism factor >> ",e_c)

plt.plot( range(n_iter),bp_e)
plt.title("Knapsack problem 1/0 >>>> Genetic Algorithm")
plt.xlabel("iteration ")
plt.ylabel(" best profit")
plt.show()
