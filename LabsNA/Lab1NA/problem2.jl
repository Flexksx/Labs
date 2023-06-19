function g(x, c)
    return 2*x - c*x^2
end

function fixed_point_iteration(c, initial_guess, num_iterations)
    p = initial_guess
    for _ in 1:num_iterations
        p = g(p, c)
    end
    return p
end

function run(c, initial_guess)
    num_iterations = 100
    limit = 1 / c
    result = fixed_point_iteration(c, initial_guess, num_iterations)
    println("Limit for c=$c: $limit")
    println("Result c=$c: $result")
end

# if we assume that it converges to 1/c, and we test for any c that
# is a positive integer, we can make the initial guess as 0.1,
# because 0 will be a root of the function

for i in 1:9
    run(i, 0.1)
end
