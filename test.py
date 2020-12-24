import re

def func(matched):
    s = ""
    for word in matched.group():
        if word != '(' and word != '[' and word != ')' and word != ']':
            s += 'I'
    s = 'B' + s[1:]
    return s

s = "即，进行如下[[[(((控制)))]]]：在[[[(((目标)))]]]张力大于规定值时，以小的设定[[[(((电阻)))]]]值修 正[[[(((控制信号)))]]]的[[[(((电压)))]]]，减[[[(((小 修)))]]]正倍率的变动，在目标张力小于规定值时，以 大的设定电阻值[[[(((修正)))]]]控制信号的电压，增[[[(((大修)))]]]正倍率的变动。"
s = s.lower()
pattern = re.compile(r'\[\[\[\(\(\([^\[^\]]*\)\)\)\]\]\]')
s = re.sub(pattern, func, s)

s = re.sub(r"\[\[\[\(\(\(", "", s)
s = re.sub(r"\)\)\)\]\]\]", "", s)
s = re.sub(r"[^B^I]", "O", s)
print(s)
