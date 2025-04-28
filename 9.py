with open("output_9.txt","w") as otp:
 with open("input_9.txt","r") as f:
   k=[]
   for line in f:
       k.append(line)
   for i in range(0,len(k)):
       if i%2!=0:
           otp.write(str(k[i]))
