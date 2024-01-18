sandwich_orders = [
    'chicken', 'veggie', 'grilled cheese', 'roast beef',
    'turkey ham', 'hotdog', 'chicken ham']
finished_sandwiches = []

print("I'm sorry, we're all out of hotdog today.")
while 'hotdog' in sandwich_orders:
    sandwich_orders.remove('hotdog')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")