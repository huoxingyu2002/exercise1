# 打开原始文本文件
with open('input.txt', 'r', encoding='utf-8') as input_file:
    original_text = input_file.read()


word = "terrible"
count = original_text.count(word)
print(f"the times of '{word}'appear：{count}")
# 将文本分割成单词
words = original_text.split()

# 初始化替换后的文本和计数器
replaced_text = []
terrible_count = 0

# 遍历每个单词并替换 "terrible"
for word in words:
    if word.lower() == "terrible":
        terrible_count += 1
        if terrible_count % 2 == 0:
            replaced_text.append("pathetic")
        else:
            replaced_text.append("marvellous")
    else:
        replaced_text.append(word)

# 将替换后的文本合并成字符串
result_text = ' '.join(replaced_text)

# 将替换后的文本写入新文件 "result.txt"
with open('result.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(result_text)

print("替换完成，并已写入 result.txt 文件。")