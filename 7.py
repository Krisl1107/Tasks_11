with open("output_7.txt","w") as otp:
 with open("input_7.txt","r") as f:
   for line in f:
     if int(str(line))!=100:
       otp.write(str(line))
