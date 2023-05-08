from typing import Union
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.docstore.document import Document
from langchain.llms import OpenAI

# from CustomLLM import *
# llm = CustomLLM()

with open('website/sprunger_resume.txt') as f:
    file_text_resume = f.read()
with open('website/about_this_app.txt') as f:
    file_text_about = f.read()
with open('website/work_and_life.txt') as f:
    file_text_bio = f.read()
sources = [
            Document(page_content=file_text_resume, metadata={"source": "Joel's resume"}),
            Document(page_content=file_text_about, metadata={"source": "About"}),
            Document(page_content=file_text_bio, metadata={"source": "Biographical info"})
           ]

# chain = load_qa_with_sources_chain(llm)
chain = load_qa_with_sources_chain(OpenAI(temperature=0))


def string_answer(question, test: Union[str, None] = None) -> str:
    if test is not None:
        return test

    return str(
        chain(
            {
                "input_documents": sources,
                "question": question,
            },
            return_only_outputs=True,
        )["output_text"]
    )


if __name__ == "__main__":
    print(string_answer("Where did Joel attend school while working at Maxim?"))

