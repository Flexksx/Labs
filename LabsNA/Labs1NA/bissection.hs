-- Define the function to find the root of
f :: Double -> Double
f x = x^2 - 2

-- Define the bisection method function
bisection :: (Double -> Double) -> Double -> Double -> Double -> Double
bisection f a b tol
  | (b - a) / 2 < tol = c
  | f c == 0 = c
  | signum (f a) == signum (f c) =$ curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh bisection f c b tol
  | otherwise = bisection f a c tol
  where
    c = (a + b) / 2

-- Main function to find the root of the function using the bisection method
main :: IO ()
main = do
  let root = bisection f 0 2 0.0001
  putStrLn $ "Root of f(x) = x^2 - 2 near x = " ++ show root
