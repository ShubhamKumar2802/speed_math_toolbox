import random
import math

class Toolkit:
    def rng(self, lower_limit, upper_limit): 
        print(f'rng: started with\nlower limit: {lower_limit}\nupper limit: {upper_limit}')
        return random.randint(lower_limit, upper_limit)
    
    def generate_random_nums(self, *limit, count=2):
        print('generate_random_nums: started')
        print(f'0: {limit[0]}')
        nums = []
        while count > 0:
            num = self.rng(limit[0][0], limit[0][1])
            if num in nums: 
                count += 1
            else: 
                nums.append(num)

            count -= 1

        print(f'generate_random_nums: retuning {nums}')
        return nums
    
class MultiplicationToolkit(Toolkit):

    def fetch_random_numbers(self, lower_limit, upper_limit):
        print('fetch_random_numbers: started')
        random_nums = self.generate_random_nums((lower_limit, upper_limit))
        print(random_nums)
        print(f'fetch_random_numbers: returning {random_nums}')
        return (random_nums)

    def fetch_consecutive_numbers(self, lower_limit, upper_limit):
        print('fetch_consecutive_numbers: started')
        random_nums = []
        num = self.rng(lower_limit, upper_limit)
        print(f'fetch_consecutive_numbers: rnd num: {num}')
        if num == upper_limit:
            print(f'fetch_consecutive_numbers: returning {(num-1, num)}')
            return (num-1, num)
        
        print(f'fetch_consecutive_numbers: returning {(num, num+1)}')
        return (num, num+1)
    
    def fetch_even_spaced_numbers(self, lower_limit, upper_limit, spacing): 
        print('fetch_even_spaced_numbers: started')
        num_a = self.rng(lower_limit, upper_limit)
        if num_a + spacing > upper_limit:
            return (num_a - spacing, num_a)

        return (num_a, num_a + spacing)

    def explain(self, num_a, num_b, ques_type):
        explaination_string = ""
        match ques_type:
            case 'Consecutive': 
                explaination_string = f'$ {num_a}^2 + {num_a} $'
            
            case 'Even-Spaced': 
                mid_spacing = {(num_b - num_a)/2}
                mid_num = num_a + mid_spacing
                ans = {math.pow(mid_num, 2)} - {math.pow(mid_spacing, 2)}
                explaination_string = '$\\begin{align}' + \
                    f' = ({mid_num} - {mid_spacing})*({mid_num} + {mid_spacing}))' + \
                    f' = ({mid_num}^2 - {mid_spacing}^2)' + \
                    f' = ({math.pow(mid_num, 2)} - {math.pow(mid_spacing, 2)})' + \
                    f' = {ans}' + \
                    '\end{align}$'
            
            case 'Random': 
                explaination_string = f'Just multiply bro :skull:'
        
        return explaination_string
    
    def ans(self, num_a, num_b):
        return num_a * num_b


class SquareRootToolkit(Toolkit): 

    def fetch_random_num(self, lower_limit, upper_limit):
        return self.rng(lower_limit, upper_limit)
    
    def ans(self, num):
        return math.sqrt(num)
    

class CubeRootToolkit(Toolkit): 

    def fetch_random_num(self, lower_limit, upper_limit):
        return self.rng(lower_limit, upper_limit)
    
    def ans(self, num):
        return math.cbrt(num)
        
        

# if __name__ == '__main__':
#     limit = (50, 100)
#     toolkit = MultiplicationToolkit()
#     rnd = toolkit.fetch_random_numbers(50, 100)
#     consec = toolkit.fetch_consecutive_numbers(50, 100)
#     print(f'random: {rnd}\nconsec: {consec}')
