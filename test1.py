li = [128,128,256,2,4,16,2,128,64,4,7,4,64,16,16,256,1,2,256,1,2,123,123,4]



print("Trong dãy số:",end=' ')
for i in li:
    print(i,end=' ')

print("\nCo nhung cap so co tich bang 256:")

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]*li[j]==256:
            print(li[i],"va",li[j],"tai vi tri",i,"va",j)
            
            for x in range(i+1,len(li)):
                if li[x] == li[i] :
                    li[x] = 0                    
            for x in range(j+1,len(li)):
                if   li[x] == li[j]:
                    li[x] = 0


                    
    
            