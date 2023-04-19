function muller(f, x0, x1, x2, tol)
    # Maximum number of iterations
    max_iter = 100
    
    for i = 1:max_iter
        # Compute quadratic coefficients
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        a = (delta2 - delta1) / (h2 + h1)
        b = a*h2 + delta2
        c = f(x2)
        
        # Compute roots of the quadratic
        discr = b^2 - 4*a*c
        if abs(b - sqrt(discr)) > abs(b + sqrt(discr))
            den = b - sqrt(discr)
        else
            den = b + sqrt(discr)
        end
        dx = -2*c / den
        
        # Check for convergence
        x3 = x2 + dx
        if abs(dx) < tol
            return x3
        end
        
        # Update points
        x0 = x1
        x1 = x2
        x2 = x3
    end
    
    # Failed to converge
    error("Maximum number of iterations reached")
end

# Test the function
f(x) = x^3 + 2x^2 + 10x - 20
root = muller(f, 1.0, 1.5, 2.0, 1e-8)
println("Root: ", root)
println("f(root): ", f(root))
