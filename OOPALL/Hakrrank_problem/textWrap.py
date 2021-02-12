import textwrap
value=input()
n=int(input())
wrapper = textwrap.TextWrapper(width=n)

word_list = wrapper.fill(text=value)

print(word_list)
