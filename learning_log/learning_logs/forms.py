from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        #为topic生成表单
        model = Topic
        #表达只包含字段text
        fields = ['text']
        #不要为字段text生成标签
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        #表达只包含字段text
        fields = ['text']
        #不要为字段text生成标签
        labels = {'text':''}
        #小部件(widget)是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。通过设置属性widgets，可覆盖Django选择的默认小部件。
        # 通过让Django使用forms.Textarea，我们定制了字段'text'的输入小部件，将文本区域的宽度设置为80列，而不是默认的40列。
        # 这给用户提供了足够的空间，可以编写有意义的条目。
        widget = {'text':forms.Textarea(attrs={'cols':80})}        
        