module MP1 where

import Data.Char
import Graphics.Gloss

-- Part 1: Polymorphic functions from types

p1_1 :: a -> b -> b
-- take in type a and type b, return type b
p1_1 _ x = x


p1_2 :: (a -> b -> c) -> (a,b) -> c
-- take in x and y, return c
-- x is a function that takes in a and b and returns c
-- y is a tuple
p1_2 f g = h where
    h = (f (fst g) (snd g))

p1_3 :: (a -> b) -> (b -> c) -> a -> c
p1_3 f g h = x where
    x = g (f h)


p1_4 :: (a -> b -> c) -> a -> (d -> b) -> d -> c
p1_4 f g h i = x where
    x = (f g (h i)) 


-- Part 2: Function implementations 


-- 1. Transposes a 2-row x 2-column tuple.
--
--    e.g., transposeTup ((1,2),(3,4)) = ((1,3),(2,4))
transposeTup :: ((a,a),(a,a))  -- input matrix
             -> ((a,a),(a,a))  -- transposed matrix
-- attempt 1:
--transposeTup f = g where
    --fst (fst g) = fst (fst f)
    --fst (snd g) = snd (fst f)
    --snd (fst g) = fst (snd f)
    --snd (snd g) = snd (snd f)
-- attempt 2: 
--transposeTup (f, g) = (x, y) where
    --(fst x) = (fst f)
    --(snd x) = (fst g)
    --(fst y) = (snd f)
    --(snd y) = (snd g)
transposeTup ((a,b),(c,d)) = ((e,f),(g,h)) where
    e = a
    f = c
    g = b
    h = d



-- 2. Sorts the elements of a 3-tuple.
--
--    e.g., sort3Tup (2,1,3) = (1,2,3)
--          sort3Tup (3,2,1) = (1,2,3)
sort3Tup :: Ord a 
         => (a,a,a)  -- input 3-tuple
         -> (a,a,a)  -- sorted 3-tuple
--sort3Tup (a,b,c) = (d,e,f) where
    --g = max a b
    --f = max g c

    --h = min a b 
    --d = min h c

    --i = max a b
    --e = min i c
sort3Tup (a,b,c)
    | (a > b && b > c) = (c,b,a)
    | (b > a && a > c) = (c,a,b)
    | (a > c && c > b) = (b,c,a)
    | (b > c && c > a) = (a,c,b)
    | (c > a && a > b) = (b,a,c)
    | otherwise = (a,b,c)



-- 3. Computes the compound interest earned.
--    e.g., compoundInterest 100 0.2 1 = 20
--          compoundInterest 100 0.2 2 = 44
compoundInterest :: Floating a 
                 => a   -- principal
                 -> a   -- rate 
                 -> Int -- num of compounding periods
                 -> a   -- amount of compound interest earned
--compoundInterest f g h = i where
    --i = (f * g) * (fromIntegral h)
    --A = P(1+ r/n)^(nt)
compoundInterest p _ 0 = p -- base case
compoundInterest p r 1 = p * r -- another base case
compoundInterest p r n = compound p (p * r) (r) (n - 1) -- call compound recursively

compound :: Floating p => p -> p -> p -> Int -> p -- compound
compound p p2 _ 0 = p2 -- compound base case
compound p p2 r 1 = ((p + p2) * r) + p2 -- compound base case 2
compound p p2 r n = compound p (((p + p2) * r) + p2) r (n - 1)

-- 4. Computes the length of the Collatz sequence starting at the input.
--
--    e.g., collatzLen 10 = 7
--          collatzLen 27 = 112
collatzLen :: Integer  -- start value of the sequence
           -> Integer  -- length of sequence
--collatzLen x = y where
    --if x / 2 == 0
        --then do
            --let y = x/2
    --else
        --y = (3 * x) + 1
collatzLen 1 = 1
collatzLen x = collatz x 1 where
    collatz :: Integer -> Integer -> Integer
    collatz 1 y = y
    collatz x y
        | odd x = collatz ((x * 3) + 1) (y + 1)
        | even x = collatz (x `div` 2) (y + 1)


-- 5. Computes the square root of the input using Newton's method.
--
--    e.g., newtonsSqrt 2 ~= 1.4142...
--          newtonsSqrt 1000 ~= 31.6227...
newtonsSqrt :: (Floating a, Ord a) 
            => a -- x
            -> a -- square root of x

--newtonsSqrt x = 
--    do
--    newtonsSqrt = improve x y
-- 0.5 * 

--newtonsSqrt x = newt 1 x where
    --newt y x = if abs (y * y - x) < 0.001
        --then y
        --else newt ((y + (x / y)) / 2) x
        -- Not sure where helper function goodEnough or improve should go..? 

newtonsSqrt x = iter (x/2) where
    iter g | g^2 =~= x = g
           | otherwise = iter (improve g)
    improve g = (g + x/g) / 2
infix 4 =~=
(=~=) :: (Floating a, Ord a) => a -> a -> Bool
x =~= y = abs (x - y) < 0.00001


-- 6. Draws a planet in a circular orbit given an orbital radius and period.
drawOrbit :: Float  -- radius
          -> Float  -- period
          -> Float  -- time
          -> Picture
drawOrbit r p t = translate x y (circleSolid 10) where
    x = (r * cos((2 * pi * t)/p)) 
    y = (r * sin((2 * pi * t)/p))
    -- stack exec mp1


-- 7. Draws a planet in an elliptical orbit based on Kepler's equation.
drawOrbit' :: Float  -- semi-major axis
           -> Float  -- eccentricity
           -> Float  -- period
           -> Float  -- time
           -> Picture
-- We need r and theta! 
drawOrbit' s e p t = translate (r * cos(theta)) (r * sin(theta)) (circleSolid 10) where
    n = meanMotion p
    m = meanAnomaly n t
    ecap = eccentricAnomaly e m

    theta = trueAnomaly e ecap
    r = heliocentricDistance e s ecap

meanMotion :: Float -> Float
meanMotion 0 = 0
meanMotion p = (2 * pi) / (p)
-- Outputs n

meanAnomaly :: Float -> Float -> Float
meanAnomaly n t = n * t
-- Outputs M

eccentricAnomaly :: Float -> Float -> Float
--eccentricAnomaly e m = m + (((e- ((1/8) * e^3))*(sin m))+((((1/2) * e^2))*(sin (2 * m)))+((((3/8) * e^3))*(sin (3 * m))))
eccentricAnomaly e m = helper e m (m + (e * sin pi)) where
    helper e m g
        | (m + (e * sin g)) =~= g = g
        | otherwise = helper e m (imp e m g)
    imp e m g = ((g+m+(e * (sin g))) / 2)      
-- Outputs E approximation
-- ecap

trueAnomaly :: Float -> Float -> Float
trueAnomaly e ecap = (2 * atan (newtonsSqrt((1 + e) / (1 - e)) * tan (ecap / 2)))
-- Outputs theta

heliocentricDistance :: Float -> Float -> Float -> Float
heliocentricDistance e s ecap = s * (1 - (e * (cos ecap)))
-- Outputs r