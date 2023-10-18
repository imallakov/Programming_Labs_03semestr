import math
import tabulate

def main():
    x1, x2, a, b = map(int, input().split())
    n = 10
    h = (x2-x1)/n
    header = [ 'number', 'x' , 'y(x)' ]
    lines = []
    count = 1
    while (x1<=x2):
        y = pow(a,b+1)/math.log(a+b)*math.tan(x1)
        line = [count,x1,y]
        lines.append(line)
        x1+=h
        count+=1

    print(tabulate.tabulate(lines, header, tablefmt="grid"))

if __name__ == "__main__":
    main()
