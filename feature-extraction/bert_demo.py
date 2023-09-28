from transformers import BertModel, BertTokenizer
import torch

# 加载BERT模型和tokenizer
bert_model = BertModel.from_pretrained('./bert/')
tokenizer = BertTokenizer.from_pretrained('./bert/')

# 输入的token序列
input_tokens = "我想去三亚的蜈支洲岛玩,啦啦啦啦啦啦啦啦"

# 使用tokenizer将输入序列转换为BERT模型的输入格式
input_ids = tokenizer.encode(input_tokens, add_special_tokens=True)
input_ids = torch.tensor([input_ids])

# 获取BERT模型的特征向量
with torch.no_grad():
    outputs = bert_model(input_ids)
    last_hidden_states = outputs.last_hidden_state
    feature_vector = last_hidden_states[:, 0, :]

# bert输出为768维，全连接线性变成300维的特征向量
linear_layer = torch.nn.Linear(768, 300)
feature_vector = linear_layer(feature_vector)

print(feature_vector)
print(feature_vector.shape)