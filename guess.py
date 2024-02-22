s1_syb = "A"
s2_syb = "A"
s3_syb = "A"

s1_max = 75
s2_max = 70
s3_max = 65


## bio  = 2.1624
## math  = 1.9485
z_score = 2.13


phyMean = 37.12
SndevPhy = 15.78

mathMean = 33.17
SndevMath = 23.47

chemMean = 35.77
SndevChem = 15.78

bioMean = 43.78
SndevBio = 15.26

# s1 = phy
#s2 = math
# s3 = chem   dont change the order

def z_cal (s1,s2,s3,math):
  
    if math == True:
      zed = ((s1 - phyMean) /SndevPhy) + ((s2 - mathMean) /SndevMath) +((s3 - chemMean) /SndevChem)
      zed /=3
    
    else:
      zed = ((s1 - phyMean) /SndevPhy) + ((s2 - bioMean) /SndevBio) +((s3 - chemMean) /SndevChem)/3
    return zed

# print(z_cal(s1_max,s2_max,s3_max,True))




def sybol_cal(sybol):
   if (sybol=="A"):
      return (75,100)
   elif (sybol=="B"):
      return(65,74)
   elif(sybol=="C"):
      return(55,64)
   elif (sybol=="S"):
      return (35,54)
   else:
      return (0,34)
   

# print(sybol_cal("S"))
   

def guess_es (z,syb1,syb2,syb3):
    count = 0
    range_s1 = sybol_cal(syb1)
    range_s2 = sybol_cal(syb2)
    range_s3 = sybol_cal(syb3)
    if z_cal(range_s1[0],range_s2[0],range_s3[0],True) > z:
      print("grette")
    else:
    #   print("chill")
        print( z_cal(range_s1[0],range_s2[0],range_s3[0],True),z)

        for s1_1 in range(range_s1[0],range_s1[1]+1) :
            for s2_2 in range(range_s2[0],range_s2[1]+1):
                for s3_3 in range(range_s3[0],range_s3[1]+1):
                    print(s1_1,s2_2,s3_3)
                    count += 1
                    print(count)


guess_es(1.9485,"A","A","C")







