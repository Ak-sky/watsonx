import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams

# Load Env Variables from .env file
load_dotenv() 
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)

# credentials object to access the LLM service
creds = Credentials(api_key, api_endpoint=api_url) 

def get_output(decoding_method):

    # Instantiate parameters for text generation, `Decoding process=sample` gives more flexible output on every execution while `Decoding process=greedy` gives more of same output on every execution
    params = GenerateParams(decoding_method=decoding_method, max_new_tokens=10)

    # Instantiate a model proxy object to send your requests
    flan_ul2 = Model("google/flan-ul2", params=params, credentials=creds)

    print("\n" + str(params).split()[0] + "\n")

    prompts = ["Hello! How are you?", "How's the weather?"]
    for response in flan_ul2.generate(prompts):
        print(response.generated_text)


get_output("sample")