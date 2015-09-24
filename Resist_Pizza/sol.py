dict = {'Anchovies':50, 'Artichoke':60, 'Bacon':92, 'Broccoli':24, 'Cheese':80,  'Chicken':30, 'Feta':99, 'Garlic':8, 'Ham':46, 'Jalapeno':5, 'Meatballs':120, 'Mushrooms':11, 'Olives':25, 'Onions':11, 'Pepperoni':80, 'Peppers':6, 'Pineapple':21, 'Ricotta':108, 'Sausage':115, 'Spinach':18, 'Tomatoes':14}
a = raw_input().split()
N = int(a[0])
mul = a[1::2]
mul = [int(i) for i in mul]
ingredient = a[2::2]
ingredient = [i.split(',') for i in ingredient]
s = sum([270*mul[i]+mul[i]*sum([dict[j] for j in ingredient[i]]) for  i in range(N)])
print 'The total calorie intake is %d' % s
