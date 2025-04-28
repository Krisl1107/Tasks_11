with open("output_6.txt","w") as otp:
 with open("input_6.txt","r") as f:
  try:
   k=[]
   for line in f:
    k.append(line)
   N=int(str(k[0]))
   if len(k)-1==N:
    otp.write("YES")
   else:
       otp.write("NO")
  except ValueError:
      otp.write("Error")
