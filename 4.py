with open("output_4.txt","w") as otp:
 with open("input_4.txt","r") as f:
  for line in f:
   if len(line)-1>20 :
       otp.write(line)
