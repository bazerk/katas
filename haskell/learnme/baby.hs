doubleMe x = x + x 
doubleUs x y = doubleMe x + doubleMe y
doubleSmallNumber x = if x > 100  
                        then x  
                        else x*2 

-- lists
-- [] empty list
-- 1:[] append to list
-- [] ++ [] join two lists (each iterm iterated over)
-- [] !! 5 get item out of list
-- lists can be compared, happens head to tail
-- [3,2,1] >= [2,10,100] = true
-- head [3,2,1] gives 3
-- tail [3,2,1] gives [2,1]
-- last [3,2,1] gives 1
-- init [3,2,1] gives [3,2]
-- length [3,2,1]
-- null [] checks if a list is empty
-- reverse [] reverses a list
-- take x [] takes x elements from list as list
-- drop x [] drops x elements from front of list
-- maximum [] gives max element from list
-- mininum [] gives min element from list
-- sum [] return sum of list elements
-- product return product of list elements
-- x `elem` [] tests for presence of x in list

-- texas ranges
-- [1..20] includes both sides
-- ['A'..'z']
-- [2, 4..20] <= smart range, forms a pattern
-- [20,19..1]
-- [1,2..] <= infinite list
-- take 24 [1,2..] <= can take x amount from infinite list

-- cycle [] <= creates infinite cycle from list elems
-- repeat x <= creates infinite list of x (equiv to cycle [x])
-- replicate x N <= creates list of x N (replicate 3 10 => [10,10,10])

-- list comprehensions
-- [x*2 | x <- [1..10]] [dothis | x <- forthis]
-- [x*2 | x <- [1..10], x*2 >= 12] [dothis | x <- forthis | ifthis, orthis, orthis]
-- xNy xs ys = [x*y | x <- xs, y <- ys]
-- boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x] 

-- tuples
-- (1,2), (1,2,3) as per python
-- [(1,2), (1,2), (1,2,3)] <- wont compile, tuples in lists need to be same
-- fst (x, y) returns x
-- snd (x, y) returns y
-- zip [1,2,3,4,5] [5,5,5,5,5] <- [(1,5),(2,5),(3,5),(4,5),(5,5)]
-- zip [1..] ["apple", "orange", "cherry", "mango"] <- [(1,"apple"),(2,"orange"),(3,"cherry"),(4,"mango")]
