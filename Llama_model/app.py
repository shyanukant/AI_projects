from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain import HuggingFaceHub

import os 
import streamlit as st

LLM_KEY = os.environ.get('SQL_MODEL_KEY')
def load_llm(prompt_template):

    # llm = CTransformers(
    #     model= 'meta-llama/Llama-2-7b-chat-hf',
    #     model_type='llama',
    #     max_new_tokens = 512 ,
    #     temperature = 0.7,
        
    # )

    llm = HuggingFaceHub(
        repo_id ='meta-llama/Llama-2-7b-chat-hf',
        huggingfacehub_api_token=LLM_KEY,
        model_kwargs={
            'tempreture': 0.7, 'max_length': 150
        }

    )

    llm_chain = LLMChain(
        
        llm = llm,
        prompt= PromptTemplate.from_template(prompt_template)
    )

    return llm_chain

st.set_page_config(layout='wide')

def main():
    st.title('Content Generator')
    user_input = st.text_input('Enter you topio for article genearaion.')
    image_input = st.text_input('Enter your topic for image generation.')

    if user_input and len(image_input) > 0:
        col, col1, col2 = st.columns([1, 2, 1])

        with col:
            st.subheader('Generated Content by Buildsocia')
            st.write('Your submitted topic for content generation: ' + user_input)
            st.write('YOur submitted topic for image generation: ' + image_input)

            prompt_template = """
                            Your a digital marketing ans SEO expert and also in social media management. 
                            Craft a captivating caption that grabs attention within the first few words on {topic}. 
                            Use a mix of emotion, curiosity, and relevance to entice readers to read the full post.
            """
            llm_call = load_llm(prompt_template)
            print(llm_call)
            result = llm_call.run(user_input)

            if len(result) > 0:
                st.info('Content Generated Successfully!!')
                st.write(result)
            else:
                st.error("Sorry, i couldn't generate content!!")

        with col1:
            st.subheader('Your content image')
            image_url = 'image.png'
            st.image(image_url)
        
        with col2:
            st.subheader('Download your content')

if __name__=='__main__':
    main()