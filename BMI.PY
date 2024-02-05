a = float (input('enter your weight: '))
b =  float (input('enter your heigt:  '))
BMI = a/(b*b)
print('YOUR BMI RESULTS:  '+str(BMI),)
if BMI < 18.5 :
    print('underweight\n '
          'you need to eat enough meals and supplement adequate nutrients ')
#thiếu cân ,bạn cần ăn uống đầy đủ và bổ sung đầy đủ các chất dinh dưỡng
elif BMI < 22.9:
    print('normal')
elif BMI < 24.0:
    print('overweight \n'
          'you need to exercise and eat scientifically')
#thừa cân,bạn cần tập thể dục và ăn uống khoa học
else  :
    print('fat \n'
          'you need to exercise and scientifically')
    
