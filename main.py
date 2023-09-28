
def process_text(text):
	translator = str.maketrans( '', '', '!"#$%&\'()*+,-.。：、，（）/:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ' )
	# 使用translate方法进行文本清理
	cleaned_text = text.translate( translator )
	while len(cleaned_text) < 100:
		cleaned_text += cleaned_text
	return cleaned_text[:100]


with open('kg-producer/item_name2content.txt', 'r', encoding='utf-8') as f:
	lines = f.readlines()
	f.close()

print(len(lines))

with open('kg-producer/item_name2content_reshape.txt', 'w', encoding='utf-8') as file:
	for line in lines:
		name, content = line.strip().split('\t')
		new_content = process_text(content)
		if len(new_content) != 100:
			print('warning!')
		file.write(name + '\t' + new_content + '\n')
	file.close()

