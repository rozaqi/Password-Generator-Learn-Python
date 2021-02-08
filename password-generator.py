import random
aplhabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
numbers = ('1234567890')
symbol = ('!@#$%^&*()_-={};<>/')
long = 16
mix = aplhabet + numbers + symbol
mixed_results = [random.choice(mix) for _ in range(long)]
password = ''.join(mixed_results)
print(password)
