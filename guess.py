
import heapq
import json
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


def out_str(data):
    output = []
    try:
        for item in data:
            parts = item.split(" # ")
            zscore, subjects = parts[0], parts[1]
            subject_values, difference = subjects.split(" :: ")
            subject1, subject2, subject3 = map(int, subject_values.split())
            output.append({
                "zscore": float(zscore),
                "Pysics": subject1,
                "maths": subject2,
                "chemestry": subject3,
                "difference": float(difference)
            })

        json_output = json.dumps(output, indent=4)
        return json_output
    except:
        return '[{"error":"Not possible"}]'
def find_indexes(array, value):
    # all_dup = []
    # all_dup = []
    
    for i in range(len(array)):
        if array[i] == value:
            all_dup.append(i)
    return all_dup


def get_closest_numbers(checking_number, numbers):
    # Create a min heap to store the differences and corresponding numbers
    min_heap = []
    # Set to store unique numbers
    unique_numbers = set()

    # Iterate through each number in the array
    for num in numbers:
        # Calculate the absolute difference between the checking number and the current number
        diff = abs(checking_number - num)
        # Push the negative difference and the number to the heap
        # This is done to simulate a max heap behavior using a min heap
        heapq.heappush(min_heap, (-diff, num))

    # Extract the 5 closest unique numbers from the heap
    closest_numbers = []
    while len(closest_numbers) < 5 and min_heap:
        _, num = heapq.heappop(min_heap)
        if num not in unique_numbers:
            closest_numbers.append(num)
            unique_numbers.add(num)

    # Return the closest numbers in sorted order
    return sorted(closest_numbers)

# s1 = phy
# s2 = math
# s3 = chem   dont change the order


def z_cal (s1,s2,s3,math=True):
    phyMean = 37.12
    SndevPhy = 15.78

    mathMean = 33.17
    SndevMath = 23.47

    chemMean = 35.77
    SndevChem = 15.78

    bioMean = 43.78
    SndevBio = 15.26
    if math == True:
      zed = ((s1 - phyMean) /SndevPhy) + ((s2 - mathMean) /SndevMath) +((s3 - chemMean) /SndevChem)
      zed /=3
    
    else:
      zed = ((s1 - phyMean) /SndevPhy) + ((s2 - bioMean) /SndevBio) +((s3 - chemMean) /SndevChem)/3
      zed /=3

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

def guess_es (z,syb1,syb2,syb3,math=True):
    final_selc = []
    seleMin = []
    seleMax = []
    global all_dup
    all_dup = []
    count = 0
    range_s1 = sybol_cal(syb1)
    range_s2 = sybol_cal(syb2)
    range_s3 = sybol_cal(syb3)
    if z_cal(range_s1[0],range_s2[0],range_s3[0],math) > z:
    #   print("grette")
      print("not working")
      return [f"{z_cal(range_s1[0],range_s2[0],range_s3[0],math)} #  {s1_1} {s2_2} {s3_3} :: value"]

    else:
        # print("chill")
        if z_cal(range_s1[1],range_s2[1],range_s3[1],math) > z:
            
            # print(z_cal(range_s1[1],range_s2[1],range_s3[1],True),z)
            # print( z_cal(range_s1[0],range_s2[0],range_s3[0],True),z)

            for s1_1 in range(range_s1[0],range_s1[1]+1) :
                # break
                for s2_2 in range(range_s2[0],range_s2[1]+1):
                    for s3_3 in range(range_s3[0],range_s3[1]+1):
                        # if len(seleMax) >= 5:
                        #    break
                        calculated_z = z_cal(s1_1,s2_2,s3_3,math)
                        if z-0.1 < calculated_z < z+0.1:
                           seleMin.append(f"{calculated_z} #  {s1_1} {s2_2} {s3_3}")
                        # if z < calculated_z < z+0.1:
                        #    seleMax.append(f"{calculated_z} {z} {s1_1} {s2_2} {s3_3}")
                        
                        
                        count += 1
                        #    if count == 5:
                        #       break
                        # print(count)
            for kkk in seleMin:
               seleMax.append(float(kkk.split("#")[0]))


            closer  = (get_closest_numbers(z,seleMax))
            for lk in closer:
               find_indexes(seleMax,lk)
            for cl in all_dup:
            #    print(seleMin[cl])
            #    break
               p  =  float(seleMin[cl].split('#')[0])
               if p <= z:
                    stin = f"{seleMin[cl]} :: {z - p}"  # Assuming you want to subtract an integer
               else:
                    stin = f"{seleMin[cl]} :: { p - z}"  # Assuming you want to subtract an integer
                  

               final_selc.append(stin)

            
            return(final_selc)
            # print(len(final_selc))
        else:
           print("not working")
# s1 = phy
# s2 = math
# s3 = chem   dont change the order


#print(out_str(guess_es(2.5185,"S","S","A",False)))







