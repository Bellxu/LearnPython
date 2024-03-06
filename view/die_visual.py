from die import Die
import pygal

die=Die()

results=[]

for roll_number in range(100):
    result=die.roll()
    results.append(result)

print(results)

frequencies=[]
#分析结果
for vaule in range(1,die.number_side+1):
    frequency=results.count(vaule)
    frequencies.append(frequency)
print(frequencies)

#对结果可视化
hist=pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')