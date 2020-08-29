from PoeNinja import Get_PoeNinja_Prices
import time 

start = time.perf_counter() 
print(0)
print(Get_PoeNinja_Prices())
print(time.perf_counter()-start)
print(Get_PoeNinja_Prices())
print(time.perf_counter()-start)

