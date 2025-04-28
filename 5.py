with open("output_5.txt","w") as otp:
 with open("input_5.txt","r") as f:
  try:
   k=[]
   for line in f:
    k.append(int(line))
   m=k[0]/k[1]+k[2]
   otp.write(str(m))
  except ValueError:
      otp.write("data Error")
  except ZeroDivisionError:
      otp.write("division by 0")
