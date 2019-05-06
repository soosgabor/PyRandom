import time
import random


print('A random program elindult...')
f=open('random.txt','a')
for i in range(0,10):
    f.write(str(i)+'. véletlenszám: '+str(random.randint(1,6))+'\n')
    
print('A random program véget ért.')
f.close