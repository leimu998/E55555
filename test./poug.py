n = int(input())
xf = list(map(int, input().split()))
kc = list(map(int, input().split()))

def jd(idx, x):
    tt = xf[idx]
    if 90 <= x <= 100:
        return xf[idx] * 4.0
    elif 85 <=  x <= 89:
        return xf[idx] * 3.7
    elif 82 <= x:
        return xf[idx] * 3.3
    elif 78 <= x:
        return xf[idx] * 3.0
    elif 75 <= x:
        return xf[idx] * 2.7
    elif 72 <= x:
        return xf[idx] * 2.3
    elif 68 <= x:
        return xf[idx] * 2.0
    elif 64 <= x:
        return xf[idx] * 1.5
    elif 60 <= x:
        return xf[idx] * 1.0
    return 0

fz,fm = 0, sum(xf)
for i in range(n):
    fz += jd(i, kc[i])
print("%.2f"%(fz / fm))
