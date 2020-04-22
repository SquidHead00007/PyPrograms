range_input = int(input("Enter a number: "))
possible_divs = list(range(1,range_input+1))
revd_rng_inpt = str(range_input)
for i in possible_divs:
    remainder = range_input % i
    if remainder == 0:
        print(i)
    