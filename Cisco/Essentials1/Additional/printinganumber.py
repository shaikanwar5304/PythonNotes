numbers=[
    #0
   [
        ['###'],
        ['# #'],
        ['# #'],
        ['# #'],
        ['###']   
    ],
    #1
    [
        ['  #'],
        ['  #'],
        ['  #'],
        ['  #'],
        ['  #']   
    ],
    #2
    [
        ['###'],
        ['  #'],
        ['###'],
        ['#  '],
        ['###']   
    ],
    #3
    [
        ['###'],
        ['  #'],
        ['###'],
        ['  #'],
        ['###']   
    ],
    #4
    [
        ['# #'],
        ['# #'],
        ['###'],
        ['  #'],
        ['  #']   
    ],
    #5
    [
        ['###'],
        ['#  '],
        ['###'],
        ['  #'],
        ['###']   
    ],
    #6
    [
        ['###'],
        ['#  '],
        ['###'],
        ['# #'],
        ['###']   
    ],
    #7
    [
        ['###'],
        ['  #'],
        ['  #'],
        ['  #'],
        ['  #']   
    ],
    #8
    [
        ['###'],
        ['# #'],
        ['###'],
        ['# #'],
        ['###']   
    ],
    #9
    [
        ['###'],
        ['# #'],
        ['###'],
        ['  #'],
        ['###']   
    ]
]
n=input('enter a number:')
for i in range(5):
    for j in n:
        print(numbers[int(j)][i][0],end=' ')
    print()