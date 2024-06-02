import requests
import os
from dotenv import load_dotenv

def run_llama_inference(nl_command):
    load_dotenv()
    if "bash" not in nl_command:
        if "code" not in nl_command:
            nl_command = "bash code to " + nl_command
        else:
            if nl_command[:4] == "code":
                nl_command = "bash " + nl_command

    API_URL = os.getenv("llama_api_url")
    headers = {
        "Accept" : "application/json",
        "Authorization": os.getenv("hf_token"),
        "Content-Type": "application/json"
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": nl_command,
        "parameters": {
            "temperature": 0.01,
            "max_new_tokens": 500
        }
    })
    return output[0]["generated_text"]


def run_phi_inference_classification(user_input):
    load_dotenv()
    API_URL = os.getenv("phi3_api_url")
    headers = {"Authorization": os.getenv("hf_token")}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    prompt = f"<|user|> Classify if the given query '{user_input}' is a 1)code generation task or a 2)code explanation task. Output only 1 or 2 based on the classified action. Dont output None as your response<|end|><|assistant|>"    
    output = query({
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 2
        }
    })
    response = output[0]["generated_text"]
    return response

def run_phi_inference_explanation(code):
    load_dotenv()
    API_URL = os.getenv("phi3_api_url")
    headers = {"Authorization": os.getenv("hf_token")}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    prompt = f"<|user|> Explain the code: \n {code} <|end|><|assistant|>"    
    output = query({
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250
        }
    })
    response = output[0]["generated_text"]
    return response


#print(run_phi_inference_classification("bash code to list all files in the current directory"))
# print(extract_code_explanation(run_phi_inference_explanation("find . -type f -exec rm {} ;")))
#print(run_llama_inference("Check if the CPU usage exceeds 80%. If it does, log a warning message to system.log with the current CPU usage"))