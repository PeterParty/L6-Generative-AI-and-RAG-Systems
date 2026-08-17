# todo: de testat
# https://www.youtube.com/watch?v=kw7qwgfVeLA

from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings

class Models:
    def __init__(self):
        self.embeddings_ollama= HuggingFaceEmbeddings(
            model_name = "BlackKakapo/stsb-xlm-r-multilingual-ro"
        )

        self.model_ollama = ChatOllama(
            model="gemma3",
            temperature=0,
        )