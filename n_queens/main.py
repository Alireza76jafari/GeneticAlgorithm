import random as r
import numpy as np
import matplotlib.pyplot as plt



def make_perm(n):
    try:
        lst = list()
        while (len(lst) < n):
            j = r.randint(0, n - 1)
            if bool(j in lst) == False:
                lst.append(j)
        return lst
    except:
        print("n is wrong number >>> _ make_perm(n)")


def make_random_array_1_100(n):
    try:
        lst = list()
        for i in range(n):
            lst.append(r.randint(1, 100))
        return lst
    except:
        print("n is wrong number >>>_make_random_array_1_100(n)")


def make_bin(n):
    try:
        lst = list()
        for i in range(n):
            lst.append(r.randint(0, 1))
        return lst
    except:
        print("n is wrong number >>> _ make_bin()")


def init_n_queens():
    global n_nq;
    n_nq =r.randint(7,50)


def eval_nqueen(arr):
    try:

        tb = 0
        vazir = list()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(i - j) == abs(arr[i] - arr[j]):
                    tb += 1
                    if bool(i in vazir) == False:
                        vazir.append(i)
                    if bool(j in vazir) == False:
                        vazir.append(j)
        tv = len(vazir)

        return tv + (10 * tb)


    except:
        print("error >>. eval_nqueen")


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

    return pop[selection_l[0]], pop[selection_l[1]]


def crossover_perm_2p(par1, par2):
    n = len(par1)
    child = []
    for i in range(n):
        child.append("null")
    p1 = r.randint(0, int(0.25 * n))
    p2 = r.randint(int(0.5 * n), int(0.8 * n))
    for s in range(0, p1 + 1):
        child[s] = par1[s]

    for t in range(p2 + 1, n):
        child[t] = par1[t]

    for j in range(p1 + 1, p2 + 1):
        if bool(par2[j] in child) == False:
            child[j] = par2[j]
        else:
            for w in range(n):
                if bool(par2[w] in child) == False:
                    child[j] = par2[w]
                    break

    return child


def crossover_perm_uni(par1, par2):
    n = len(par1)
    mask = make_bin(n)
    child = []
    for ind in range(n):
        child.append("null")

    for i in range(n):
        if mask[i] == 1:
            child[i] = par1[i]
    for j in range(n):
        if mask[j] == 0 and bool(par2[j] in child) == False:
            child[j] = par2[j]
        elif mask[j] == 0 and bool(par2[j] in child) == True:
            for t in range(n):
                if bool(par2[t] in child) == False:
                    child[j] = par2[t]
                    break

    return child


def tweak_perm(arr):
    n = len(arr)
    ind1 = r.randint(0, n - 1)
    ind2 = r.randint(0, n - 1)
    ind3 = r.randint(0, n - 1)
    ind4 = r.randint(0, n - 1)
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
    arr[ind3], arr[ind4] = arr[ind4], arr[ind3]
    tweak_arr = arr

    return tweak_arr


def min_chr(arr):
    minim = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < minim:
            minim = arr[i]
            index = i
    return index


def show_chess(arr,n_nq):
    if n_nq<=50:
        for i in range(n_nq+1):
            plt.plot([0,2*n_nq],[i*2,i*2])
            plt.plot([i*2,i*2],[0,2*n_nq])
        for i in range(n_nq):
            plt.scatter([2*i +1],[arr[i]*2+1])
        plt.show()


        
def choose_elite(ar_p, ar_e, c=1):
    for i in range(c):
        best_ind = min_chr(ar_e)
        best_chr.append(ar_p[best_ind])
        best_eval.append(ar_e[best_ind])
        ar_p.pop(best_ind)
        ar_e.pop(best_ind)


# Genetic algorithm


# Primary population production

#

init_n_queens()
n_pop =r.randint(50,300)
pop = list()
n_iter = r.randint(10, 50)
best_chr = list()
best_eval = list()
eval_pop = list()
for i in range(n_pop):
    ch = make_perm(n_nq)
    pop.append(ch)
    eval_pop.append(eval_nqueen(ch))

# select and save  best Chromosome
# best_chr.append(pop[min_chr(eval_pop)])
# best_eval.append(eval_pop[min_chr(eval_pop)])
e_c =r.randint(1,8)
choose_elite(pop, eval_pop, c=e_c)

# iteration phase

itere = 0
conf=list()
b_sol=list()
while (itere < n_iter):
    itere += 1
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
        if (mutation_prob <= 0.3):
            new_pop[ch] = tweak_perm(cr)

        new_eval_pop.append(eval_nqueen(new_pop[ch]))

    pop = new_pop
    eval_pop = new_eval_pop
    choose_elite(pop, eval_pop, c=e_c)
    b_index=min_chr(best_eval)
    conf.append(best_eval[b_index])
    b_sol.append(best_chr[b_index])
    if bool(0 in best_eval) == True:
           break

    best_chr = best_chr[e_c:2 * e_c]
    best_eval = best_eval[e_c:2 * e_c]

    if itere == (n_iter - 1):
        n_iter += 1

        

        
b_index=min_chr(conf)
print(" SOLUTION FOR N_QUEENS " + str(n_nq) + "x" + str(n_nq) + " PROBLEM IS :  \n")
print(b_sol[b_index])
print(" Total CONFLICT \n: ", conf[b_index])
print("iteration >> ", itere)
print("elitism factor ",e_c)
show_chess(b_sol[b_index],n_nq=n_nq)

plt.plot(range(itere),conf)
plt.title("N_QUEENS problem  >>>> Genetic Algorithm")
plt.xlabel("iteration")
plt.ylabel(" Best Total CONFLICT")
plt.show()