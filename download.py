import os


def prepare_data():
    os.system('mkdir -p /app/model')
    download_demo()
    download_sentence_transformer()
    download_paraphrase_multilingual_MiniLM_L12_v2()
    download_NLTK()


def download_sentence_transformer():
    # 设置环境变量
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

    # 下载模型
    os.system(
        'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir ~/model/sentence-transformer')


def download_paraphrase_multilingual_MiniLM_L12_v2():
    os.system(
        'cd /app/model && git clone https://www.modelscope.cn/Ceceliachenen/paraphrase-multilingual-MiniLM-L12-v2.git && cd /app/model/paraphrase-multilingual-MiniLM-L12-v2 && git lfs install && git lfs pull ')


def download_NLTK():
    os.system(
        'cd /app && git clone https://gitee.com/yzy0612/nltk_data.git  --branch gh-pages && cd /app/nltk_data && mv /app/nltk_data/packages/*  /app/nltk_data && cd /app/nltk_data/tokenizers && unzip punkt.zip && cd /app/nltk_data/taggers && unzip averaged_perceptron_tagger.zip')


def download_demo():
    os.system(
        'mkdir /app/data && cd /app/data && git clone https://github.com/Kit-Hung/demos && cp /app/data/demos/blob/main/k8s/1-deploy/3-k8s_install/2-kubeadm/kubeadm.md /app/data')


prepare_data()
