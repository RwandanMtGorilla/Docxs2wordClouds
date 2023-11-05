# 词云生成脚本

## 项目介绍
这个脚本用于从Word文档中读取文本内容，通过结巴分词进行中文分词处理，并生成词云图像。此外，该脚本还支持从停用词列表中过滤出不需要的词汇，以便生成更加准确和有用的词云。

## 环境要求
- Python 3.x
- python-docx
- jieba
- wordcloud
```
pip install python-docx jieba wordcloud
```

## 使用方法
将Word文档放置在项目目录下的input文件夹中。
确保stopwords.txt文件（包含要排除的停用词）位于项目根目录中。
运行脚本：
```
python word_cloud_generator.py
```
生成的词云图片将保存为wordcloud.png。

## 文件结构
```yaml
word_cloud_generator.py: 主脚本，用于生成词云。
input/: 文件夹，用于存放Word文档。
stopwords.txt: 文本文件，包含停用词列表。
wordcloud.png: 输出文件，生成的词云图片。
```
