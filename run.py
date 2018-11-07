import random


class GenerateRandomNum():
    """docstring for GenerateRandomNum"""

    def check_user_input(self, input, rand):
        if (int(input) == " "):
            return "No input provided"
        else:
            if (int(input) > rand):
                return "Your selection is higher than"
            elif (int(input) < rand):
                return "Your selection is lower"
            elif (int(input) < 0 or int(input) > 6):
                return "User input is above range"
            elif (int(input) == rand):
                return True


def user_input():
    input_num = input("Please enter a number:")
    return int(input_num)


run_app = GenerateRandomNum()
random_num = random.randint(1, 6)
user_data = user_input()

resp = run_app.check_user_input(user_data, random_num)
if resp == True:
    print("You win")
else:
    print(resp)
