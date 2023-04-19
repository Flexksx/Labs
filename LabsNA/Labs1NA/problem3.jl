function f(x)
    return x^3+2*x^2+10*x-20
end

x=zeros(100)
x[1]=0
x[2]=1
x[3]=2

for i=4:length(x)-1
    if f(x[i-1])==0.0
        print("Solution found: ", x[i-1])
        break
    end
    q=(x[i-1]-x[i-1-1])/(x[i-1-1]-x[i-1-2])
    c=(1+q)*f(x[i])
    b=(2*q+1)*f(x[i-1])-(1+q)^2*f(x[i-1-1])+q^2*f(x[i-1-2])
    a=q*f(x[i-1])-q*(1+q)*f(x[i-1-1])+q^2*f(x[i-1-2])
    Δ=b^2-4*a*c
    if isreal(sqrt(Δ))
        x1=b-sqrt(Δ)
        x2=b+sqrt(Δ)
        jopa=max(x1,x2)
    else 
        x1=b-sqrt(Complex(Δ))
        x2=b+sqrt(Complex(Δ))
        jopa=max(x1,x2)
    end
    x[i]=x[i-1]-(x[i-1]-x[i-1-1])*(2*c)/jopa
end

for i=1:length(x)
    print("x[",i,"]=",x[i]," f(x)=",f(x[i]),"\n")
end
