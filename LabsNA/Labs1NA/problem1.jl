function f(x)
    return exp(x)-x*x
end

function bisection(low, up, tol)
    if f(low)*f(up) >= 0
        return "error",0
    end
    mid = (low + up)/2
    n = 0    
    while abs(f(mid)) > tol
        n += 1
        if f(low)*f(mid) < 0
            up = mid
        else
            low = mid
        end
        mid = (low + up)/2
    end
    return mid, n
end

sol,i=bisection(-2,0,1e-8)
if sol=="error"
    print("The signs of the bounds are not opposite")
end
print("Solution is ", sol, " after ", i," iterations" )