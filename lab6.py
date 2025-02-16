# Mapper
import sys

for line in sys.stdin:
    line = line.strip()
    details = line.split()
    
    title = details[1]
    state = details[3]  
    salary = int(details[4])
    
    print("%s%s\t%d" % (title, state, salary))

# Reducer 
import sys

current_key = None  
key_sum = 0
key_count = 0

for line in sys.stdin:
    line = line.strip()  
    key, value = line.split("\t") 
    
    value = int(value)
    
    if key == current_key:
        key_sum += value
        key_count += 1

    else:
        if current_key:            
            avg_salary = key_sum/key_count
            print("%s\t%d" % (current_key, avg_salary))
            
        current_key = key        
        key_sum = value
        key_count = 1
        
if current_key == key:

    avg_salary = key_sum/key_count
    print("%s\t%d" % (current_key, avg_salary))
