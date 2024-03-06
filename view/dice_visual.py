from die import Die
import pygal

die1=Die()
die2=Die()

results=[]

for roll_num in range(1000):
    result=die1.roll() + die2.roll()
    results.append(result)
#分析结果
frequencies=[]
max_result=die1.number_side+die2.number_side
for vaule in range(2,max_result+1):
    frequency=results.count(vaule)
    frequencies.append(frequency)

hist=pygal.Bar()
hist.title="Results of rolling two D6 dice in 1000 times"
hist.x_labels=range(2,die1.number_side+die2.number_side+1)
hist.x_title="Result"
hist.y_title="Frequency of result"
hist.add("D6+D6",frequencies)
hist.render_to_file("dice_visual.svg")
#可视化展示
