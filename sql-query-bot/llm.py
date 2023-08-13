## Creating a LLM using LangChain + HuggingFace
import os
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

hf_key = os.environ.get("SQL_MODEL_KEY")
hub_llm = HuggingFaceHub(repo_id="mrm8488/t5-base-finetuned-wikiSQL", huggingfacehub_api_token=hf_key)

prompt = PromptTemplate(
    input_variables= ['question'],
    template= "please translate it into SQL query! {question}",
)

chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
print(chain.run("Give me distance of london and when airport number is EG8 from flight table."))