with open("output_2.txt","w") as otp:
 with open("input_2.txt","r") as f:
  for line in f:
   if line[0]=="A" or line[0]=="a" :
       otp.write(line)
