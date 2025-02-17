eggs = int(input('how meny eggs: '))
cartion = 0
left_over = 0
while eggs > 6:
    eggs = eggs - 6
    cartion = cartion + 1
print('you have:', eggs, 'leftover and', cartion, 'carton\'s used')