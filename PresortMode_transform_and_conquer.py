def PresortMode(A):
    i=0
    modefrequency=0
    n=len(A)
    while i<=n-1:
        runlength=n-1
        runvalue=A[i]
        while i+runlength<=n-1 and A[i+runlength]==runvalue:
            runlength=runlength+1
        if runlength>modefrequency:
            modefrequency=runlength
            modevalue=runvalue
        i=i+runlength
    return modevalue
PresortMode()
