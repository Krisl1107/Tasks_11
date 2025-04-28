with open("output_3.txt","w") as otp:
 with open("input_3.txt","r") as f:
  for line in f:
    otp.write(line[0])
