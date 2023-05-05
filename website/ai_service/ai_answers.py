from typing import Union
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.docstore.document import Document
from langchain.llms import OpenAI

# from CustomLLM import *
# llm = CustomLLM()

with open('website/sprunger_resume.md') as f:
    file_text = f.read()
sources = [Document(page_content=file_text, metadata={"source": "Joel's resume"})]

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

