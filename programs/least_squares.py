def main():
    x=[30,60,90,120]
    y=[16,22,23,26]
    least_squares(x,y)

    
def least_squares(x,y):
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    y1=0
    xy=0
    x2y=0
    x3y=0 
    for i in range(len(x)):
        x1+=x[i]
        x2+=x[i]**2
        x3+=x[i]**3
        x4+=x[i]**4
        x5+=x[i]**5
        x6+=x[i]**6
        y1+=y[i]
        xy+=x[i]*y[i]
        x2y+=x[i]**2*y[i]
        x3y+=x[i]**3*y[i]
    print("Equations: ")
    print("Linear model")
    print(f"{len(x)}a0 + {x1}a1 = {y1}")
    print(f"{x1}a0 + {x2}a1 = {xy}")

    print("Quadratic model")
    print(f"{len(x)}a0 + {x1}a1 + {x2}a2 = {y1}")
    print(f"{x1}a0 + {x2}a1 + {x3}a2 = {xy}")
    print(f"{x2}a0 + {x3}a1 + {x4}a2 = {x2y}")

    print("Cubic model")
    print(f"{len(x)}a0 + {x1}a1 + {x2}a2 + {x3}a3 = {y1}")
    print(f"{x1}a0+{x2}a1+{x3}a2+{x4}a3={xy}")
    print(f"{x2}a0 + {x3}a1 + {x4}a2 + {x5}a3={x2y}")
    print(f"{x3}a0+{x4}a1+{x5}a2+{x6}a3={x3y}")
    return


if __name__ == "__main__":
    main()