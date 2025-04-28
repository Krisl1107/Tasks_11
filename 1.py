with open("input_1.txt","r") as f:
  k=0
  for line in f:
    k=line.upper()
with open("output_1.txt","w") as otp:
    otp.write(str(k))
