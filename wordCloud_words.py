import os
import jieba
from wordcloud import WordCloud
from docx import Document

def read_docx(file_path):
    """ 读取Word文档内容 """
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def load_stopwords(file_path):
    """ 读取停用词列表 """
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = set([line.strip() for line in file])
    return stopwords

def generate_word_cloud(text, file_name, stopwords):
    """ 生成词云并保存为图片 """
    wordcloud = WordCloud(font_path='C:\\Windows\\Fonts\\msyh.ttc', width=800, height=800, background_color='white', stopwords=stopwords).generate(text)
    wordcloud.to_file(file_name)

input_folder = 'input/'
stopwords_file = 'stopwords.txt'
texts = []

# 读取停用词列表
stopwords = load_stopwords(stopwords_file)

# 遍历input文件夹读取所有Word文档
for file in os.listdir(input_folder):
    if file.endswith('.docx'):
        file_path = os.path.join(input_folder, file)
        texts.append(read_docx(file_path))

# 将所有文档内容合并，并进行结巴分词
combined_text = ' '.join(texts)
seg_list = jieba.cut(combined_text, cut_all=False)
seg_text = ' '.join([word for word in seg_list if word not in stopwords])

# 生成词云
generate_word_cloud(seg_text, 'wordcloud.png', stopwords)
