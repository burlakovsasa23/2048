from tkinter import*
from random import*

size = 6
Sz = 400
V = [[0 for i in range(size)] for j in range(size)]

root = Tk()
C = Canvas(width = Sz, height = Sz)
C.pack()

def log(x):
    #print(x)
    if abs(x) == 2:
        return 0
    return log(x // 2) + 1

def Vis():
    C.delete("all")
    AP = ["red", "orange", "yellow", "green", "#00ffff", "blue", "purple", "pink", "#ff0088", "#ff0044", "#ff2222"]
    AM = ["darkred", "brown", "#888800", "darkgreen", "#008888", "darkblue", "#880088", "purple", "#880044", "#880022", "#881111"]
    for i in range(size):
        for j in range(size):
            K = (Sz - 20) // size
            if V[i][j] == 0:
                C.create_rectangle(K * i + 10, K * j + 10, K * (i + 1) + 10, K * (j + 1) + 10, width = 20)
            else:
                if V[i][j] > 0:
                    C.create_rectangle(K * i + 10, K * j + 10, K * (i + 1) + 10, K * (j + 1) + 10, fill = AP[log(V[i][j])], width = 20)
                else:
                    C.create_rectangle(K * i + 10, K * j + 10, K * (i + 1) + 10, K * (j + 1) + 10, fill = AM[log(V[i][j])], width = 20)
                C.create_text(K * (i + 0.5) + 10, K * (j + 0.5) + 10, text = str(V[i][j]), font = "Courier " + str(int(0.75 * Sz // size // len(str(V[i][j])) // 1)))
            

def Gen():
    
    x = randint(0, size - 1)
    y = randint(0, size - 1)
    while V[x][y] != 0:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
    if randint(1, 2)  == 1:
        ans = -1
    else:
        ans = 1
    if randint(1, 10) == 1:
        V[x][y] = 4 * ans
    else:
        V[x][y] = 2 * ans

def TL():
    global V, size
    #(x, y) -> (-y, x)
    New = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            size -= 1
            X = size - 2 * i
            Y = size - 2 * j
            #print(X, Y)
            X, Y = X, -Y
            #print(X, Y)
            x = (size - X) // 2
            y = (size - Y) // 2
            #print(i, j, x, y)
            New[x][y] = V[i][j]
            size += 1
    V = [[New[i][j] for i in range(size)] for j in range(size)]

def Left():
    global V
    L = []
    for i in range(size):
        S = []
        r = 0
        for j in range(size):
            if V[i][j] == 0:
                continue
            if r == 0:
                S.append(V[i][j])
                r = V[i][j]
            else:
                if V[i][j] == r:
                    S[-1] += V[i][j]
                    r = 0
                else:
                    S.append(V[i][j])
                    r = V[i][j]
        while len(S) < size:
            S.append(0)
        #print(V[i], S)
        L.append(S)
    if V == L:
        return 1
    V = [[L[j][i] for i in range(size)] for j in range(size)]

Vis()

def Tr(event):
    Vis()
    if event.keysym == "w":
        if Left():
            Gen()
            return
    elif event.keysym == "d":
        TL()
        TL()
        TL()
        if Left():
            Gen()
            return
        TL()
    elif event.keysym == "s":
        TL()
        TL()
        if Left():
            Gen()
            return
        TL()
        TL()
    elif event.keysym == "a":
        TL()
        if Left():
            Gen()
            return
        TL()
        TL()
        TL()
    else:
        return
    Gen()
    Vis()
    

C.bind_all("<Key>", Tr)
root.mainloop()
