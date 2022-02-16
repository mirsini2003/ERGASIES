
import random
import numpy as np
#arxikopoihsh twn vathmwn
pq=0
op=0
#dimiourgia skakieras
board= [[1, 2, 3, 4, 5, 6, 7, 8], 
        [1, 2, 3, 4, 5, 6, 7, 8], 
        [1, 2, 3, 4, 5, 6, 7, 8], 
        [1, 2, 3, 4, 5, 6, 7, 8], 
	    [1, 2, 3, 4, 5, 6, 7, 8], 
    	    [1, 2, 3, 4, 5, 6, 7, 8], 
    	    [1, 2, 3, 4, 5, 6, 7, 8], 
	    [1, 2, 3, 4, 5, 6, 7, 8]]
for k in range(1, 101):
    qx = 1 + random.randrange(7) 
    qy = 1 + random.randrange(7) 
    bx = 1 + random.randrange(7) 
    by = 1 + random.randrange(7) 
    rx = 1 + random.randrange(7) 
    ry = 1 + random.randrange(7) 
    # If queen and the opponent are
    # in the same row
    if qx == bx:
        pq=pq+1
    if qx == rx:
        op=op+1
    if qy == by:
        pq=pq+1
    if qy == ry:
        op=op+1
    if abs(qx - bx) == abs(qy - by):
        op=op+1
    if abs(qx - rx) == abs(qy - ry):
        pq=pq+1
print("Οι βαθμοί των παικτών μετά από 100 γύρους ειναι: " , op , " και " ,pq ," αντιστοιχα.")
    
    