##############################################
# Sigma laby by a sigma!
# the date is feb 14thhhhh
# https://github.com/lucars1
##############################################

totalmakrs = 0
for i in range (0, 4):
    mark = int(input('mark NOW: '))
    totalmakrs = totalmakrs + mark
    if mark > 100:
        print('dont lie')
        exit()
mark_ave = totalmakrs / 4

if mark_ave < 50:
    print('you failed dumb dumb')

if mark_ave > 50 and mark_ave < 59:
    print('zoinks close one! ', mark_ave)
    
if mark_ave > 60 and mark_ave < 69:
    print('Could do better', mark_ave)
    
if mark_ave > 70 and mark_ave < 79:
    print('Meh you got a level 3', mark_ave)
    
if mark_ave > 80 and mark_ave < 101:
    print('smorty pants you got: ', mark_ave,'%')