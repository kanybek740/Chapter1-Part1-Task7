
# Write a function biggest_guy that takes in three numbers as input and returns the biggest one.
# Ex: biggest_guy(10, 30, 20) # --> 30
# BONUS CHALLENGE: Write a 1 line solution (Medium Difficulty)
    

# list1 = list(input('napiwi cifru :'))

def biggest_guy(one, two, three):
#write your code here ...
    return max(one, two, three)
# print(biggest_guy(list1[0],list1[1],list1[2]))
#     
# def bigger_guy(num1, num2): 
#     if num1 > num2:
#         return num1
#     else:
#         return num2


# def biggest_guy(num1, num2, num3):

  # find bigger guy between num1 and num2
  # find biggest guy between bigger guy and num3
#   return bigger_guy(bigger_guy(num1, num2), num3)
def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30    
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("WRONG!!")
        return
    print("SUCCESS!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()