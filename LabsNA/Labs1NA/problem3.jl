f(x) = x^3+2*x^2+10*x-20

function muller(f, x0, x1, x2, tol)
    max_iter = 100
    
    for i = 1:max_iter
        h1 = x1 - x0
        h2 = x2 - x1
        δ1 = (f(x1) - f(x0)) / h1
        δ2 = (f(x2) - f(x1)) / h2
        a = (δ2 - δ1) / (h2 + h1)
        b = a*h2 + δ2
        c = f(x2)
        dis = b^2 - 4*a*c
        if abs(b - sqrt(dis)) > abs(b + sqrt(dis))
            jopa = b - sqrt(dis)
        else
            jopa = b + sqrt(dis)
        end
        dx = -2*c / jopa
        x3 = x2 + dx
        if abs(dx) < tol
            return x3
        end
        x0 = x1
        x1 = x2
        x2 = x3
    end
    error("Too many iterations")
end

r=muller(f,0,1,2,1e-8)
print("Root is r=",r,"\n")
print("f(r)=",f(r))