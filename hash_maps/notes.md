hashmap store key-value pairs

it provide 
O(1) look at -> worst case is O(n) is we have hashing collisions
O(1) adding -> worst case is O(n) is we have hashing collisions
O(1) remove -> worst case is O(n) is we have hashing collisions
O(1) getSize()


using a Linkelist to implement the hasmap 

if we get a hashing collision we can use chaining to take care of that (e.g lets say 2 value share the same key the value would be in a chain
like this 1 -> 2)