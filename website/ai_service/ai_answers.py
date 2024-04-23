from typing import Union

from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# from CustomLLM import *
# llm = CustomLLM() <<- use a custom LLM

with open('website/sprunger_resume.txt') as f:
    file_text_resume = f.read()
with open('website/about_this_app.txt') as f:
    file_text_about = f.read()
with open('website/biographical.txt') as f:
    file_text_bio = f.read()
with open('website/interview_faq.txt') as f:
    file_text_faq = f.read()

sources = [
            Document(page_content=file_text_about, metadata={"source": "About this app"}),
            # Document(page_content=file_text_faq, metadata={"source": "Interview FAQ"}),
            Document(page_content=file_text_bio, metadata={"source": "Biographical info"}),
            Document(page_content=file_text_resume, metadata={"source": "Joel's resume"})
           ]

source_chunks = []
splitter = CharacterTextSplitter(separator=" ", chunk_size=1024, chunk_overlap=0)
for source in sources:
    for chunk in splitter.split_text(source.page_content):
        source_chunks.append(Document(page_content=chunk, metadata=source.metadata))

search_index = FAISS.from_documents(source_chunks, OpenAIEmbeddings())

# chain = load_qa_with_sources_chain(llm)
chain = load_qa_with_sources_chain(ChatOpenAI(model="gpt-4", temperature=0))


def string_answer(question, test: Union[str, None] = None) -> str:
    if test is not None:
        return test

    return str(
        chain(
            {
                "input_documents": search_index.similarity_search(question, k=4),
                "question": question,
            },
            return_only_outputs=True,
        )["output_text"]
    )


if __name__ == "__main__":
    print(string_answer("Where did Joel attend school?"))

