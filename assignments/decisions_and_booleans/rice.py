rice_order_remaining_str = input('Enter the amount of rice to buy (kg): ')
rice_order_remaining_float = float(rice_order_remaining_str)

soy_sauce_str = input('Enter the amount of soy sauce (bottles): ')
soy_sauce_int = int(soy_sauce_str)

total_rice_cost = 0
total_soy_cost = 0

soy_sauce_discount_threshold = 10
soy_sauce_discount = 0.1
soy_sauce_price = .99

step_1_weight = 25
step_1_price = 4.84

step_2_weight = 20.2
step_2_price = 3.89

step_3_price = 2.99


# step 1: first 25kg
if rice_order_remaining_float > 0:
    total_rice_cost += step_1_price * min(step_1_weight, rice_order_remaining_float)
    rice_order_remaining_float = round(rice_order_remaining_float - step_1_weight, 5)

# step 2: next 20.2 kg
if rice_order_remaining_float > 0:
    total_rice_cost += step_2_price * min(step_2_weight, rice_order_remaining_float)
    rice_order_remaining_float = round(rice_order_remaining_float - step_2_weight, 5)

# step 3: rest
if rice_order_remaining_float > 0:
    total_rice_cost += step_3_price * rice_order_remaining_float

if soy_sauce_int > 0:
    total_soy_cost = soy_sauce_int * soy_sauce_price

if soy_sauce_int >= soy_sauce_discount_threshold:
    total_rice_cost *= (1-soy_sauce_discount)


print('Total price is: $', total_rice_cost + total_soy_cost)
