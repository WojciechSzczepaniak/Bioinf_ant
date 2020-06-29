from random import randint
import numpy
import time

def problem_init(data,l):
    d_len = len(data)
    matrix = [[l for i in range(d_len)] for y in range(d_len)]
    pheromone = [[1 for i in range(d_len)] for y in range(d_len)]
    for i in range(d_len):
        for j in range(d_len):
            x = data[i]
            y = data[j]
            for e in range(l-1):
                x1 = x[e:l]
                x2 = y[0:l-e]
                if x1 == x2 and i != j:
                    matrix[i][j] = e
                    break
    return(matrix, pheromone, d_len)

def main(matrix1,pheromone,d_len, n, l1, n_ants, n_it, f_path1,af,best_path,sterowanie):
    ants = []
    for i in range(n_ants):
        ants.append((10, []))
    for i in range(n_it):
        print(i)
        for y in range(n_ants):
            x = list(ants[y])
            ni = randint(0,d_len-1)
            x[1] = [ni]
            ant = []
            ant.append(x[1][-1])
            acc = x[0]
            while(x[0] < n-l1):
                y = ant[-1]
                next_path = matrix1[y]

                next_to_choose = [0 for i in range(len(next_path))]
                next_to_choose = prawdopodobienstwo(pheromone[y],next_path,next_to_choose,sterowanie)
                next_wi = numpy.random.choice(numpy.arange(0, len(next_to_choose)), p=next_to_choose)
                if(next_wi not in ant):

                    if((x[0] + next_path[next_wi]) > n-l1):
                        for i in range(len(next_path)):
                            if(((x[0] + next_path[i]) < n-l1) and i not in ant):
                                acc = x[0]
                                x[0] = x[0] + next_path[i]
                                if(x[0] > n-l1):
                                    pass
                                else:
                                    acc = x[0]
                                    ant.append(i)
                        if(x[0] < n-l1):
                            acc = x[0]
                            x[0] = x[0] + next_path[i]
                            if (x[0] > n - l1):
                                pass
                            else:
                                acc = x[0]
                                ant.append(next_wi)
                    else:
                        acc = x[0]
                        x[0] = x[0] + next_path[next_wi]
                        if (x[0] > n - l1):
                            pass
                        else:
                            acc = x[0]
                            ant.append(next_wi)

            pheromone = phero_update(pheromone, ant, acc)
            if(len(best_path)<len(ant)):
                best_path = ant
                dg = acc
        pheromone = phero_update(pheromone,best_path,dg)
        pheromone = parowanie(pheromone,sterowanie[2])
    return(best_path)

def phero_update(pheromone,best_path,dg):
    koszt = dg
    dodatek = len(best_path)*len(best_path)/koszt
    for i in range(len(best_path)-1):
        g = best_path[i]
        g2 = best_path[i+1]
        pheromone[g][g2] = pheromone[g][g2] + dodatek
    return(pheromone)

def parowanie(pheromone, alfa):
    for i in range(len(pheromone)):
        for j in range(len(pheromone)):
            pheromone[i][j] = pheromone[i][j]*alfa
    return(pheromone)

def prawdopodobienstwo(feromon, atrakcyjnosc,next_to_choose,sterowanie):
    sumed = 0
    for i in range(len(next_to_choose)):
        sumed += (feromon[i]**sterowanie[0])*((1/atrakcyjnosc[i])**sterowanie[1])
    for i in range(len(next_to_choose)):
        next_to_choose[i] = (feromon[i]**sterowanie[0])*((1/atrakcyjnosc[i])**sterowanie[1])/sumed
    return(next_to_choose)

if __name__ == "__main__":
    params = [209, 10, 200, 5, "instances/1.txt", 1]
    start_time = time.time()
    n = params[0]
    l1 = params[1]
    n_ants = params[2]
    n_it = params[3]
    f_path1 = params[4]
    af = params[5]
    best_path = []
    sterowanie = [1,1,0.95]
    f = open(f_path1, "r")
    data = f.readlines()

    matrix1, pheromone, d_len = problem_init(data, l1)
    best = main(matrix1, pheromone, d_len, n, l1, n_ants, n_it, f_path1, af, best_path,sterowanie)
    print(best)
    print(len(best))
    print("--- %s seconds ---" % (time.time() - start_time))

