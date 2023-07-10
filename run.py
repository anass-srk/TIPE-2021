import sys
import numpy as np

from monobit import monobit_test

if len(sys.argv) != 2 :
  print("The generated bin file is required as an input !")
  exit(-1)

with open(sys.argv[1],"rb") as file :
  bitlist = np.unpackbits(np.fromfile(file,dtype=np.uint8))
  (success,p) = monobit_test(bitlist)
  print(" p-value is : ",p)
  print(" SUCCESS !" if success else " TEST FAILED !")
