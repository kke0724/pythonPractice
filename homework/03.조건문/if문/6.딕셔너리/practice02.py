score = {'kor': 90, 'en':45}
print(score)
score['math'] = 100
print(score)
score['en'] = 80
print(score)
x = score.pop('math')
print(x)
print(score)

score.clear()
print(score)