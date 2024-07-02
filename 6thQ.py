# Pavan Vitesh Kuncham - AP21110011080 - Q.No - 6
numbers = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 7] # these are 0 to 11
tys = [0, 0, 6, 6, 6, 5, 5, 7, 6, 5] # all ty's like twenty, thirty, fourty

# Function to calculate count for numbers before 20
def find_till_20(n):
    return numbers[n]
    
# Function to calcuate count for numbers fron 20 till 99
def find_for_twos(n):
    if n < 20:
        return find_till_20(n)
    else:
        return tys[n//10] + numbers[n%10]
     
# Function to count for 3 digit numbers   
def find_for_threes(n):
    return numbers[n//100] + 7 + find_for_twos(n%100)

# support for main function
def find_len(n):
    if n < 100:
        return find_for_twos(n)
    else:
        return find_for_threes(n)
    
# Main calling function
def find_for_1000(): 
    cnt = 11 # considered for 1000 at first since it is the only 4 digit number
    for i in range(1,1000):
        cnt += find_len(i)
    return cnt
    
print("Sum of word lenths till 1000 is : ", find_for_1000())