import torch
from torchvision import transforms, models
from PIL import Image

# 图像预处理
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 定义resnet18网络
model = models.resnet18(True)
model.fc = torch.nn.Linear(512, 1024)

# 药材列表和特征向量列表初始化
herbs = []
features = []

# 循环加载本地图片
with open("./herbs.txt", encoding='utf-8') as fr:
    herb_list = fr.read().split()
    print("共有{}种药材".format(len(herb_list)))
    for h in herb_list:
        print("抽取{}的特征".format(h))
        img_path = "./herb_complete/" + str(h) + ".jpg"
        image = Image.open(img_path).convert("RGB")
        image_tensor = torch.unsqueeze(preprocess(image), 0)
        # 调用编码器模型
        feature = model(image_tensor)
        # 保存到列表
        herbs.append(h)
        features.append(feature)


assert len(herbs) == len(features), "num error"

print("\n正在写入文件...")
length = len(herbs)
with open("herb_img_result.txt", "w", encoding='utf-8') as fw:
    for i in range(length):
        fw.write(herbs[i])
        numpy_feature = features[i].detach().numpy()[0]
        for n in numpy_feature:
            fw.write(" ")
            fw.write(str(n))
        fw.write("\n")

