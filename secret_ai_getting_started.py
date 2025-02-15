import os
from secret_ai_sdk.secret_ai import ChatSecret
from secret_ai_sdk.secret import Secret

# Set API key (REPLACE WITH YOUR KEY)
os.environ["SECRET_AI_API_KEY"] = "bWFzdGVyQHNjcnRsYWJzLmNvbTpTZWNyZXROZXR3b3JrTWFzdGVyS2V5X18yMDI1"

secret_client = Secret()
models = secret_client.get_models()
urls = secret_client.get_urls(model=models[0])
secret_ai_llm = ChatSecret(
base_url=urls[0], # in this case we choose to access the first url in the list

model='llama3.1:70b', # your previosly selected model
temperature=1.
)
# Define your messages you want to send to the confidential LLM for processing
messages = [
    ("system", "You are my therapist. Help me with my issues."),
    ("human", "I miss my cat."),
]

response = secret_ai_llm.invoke(messages, stream=False)
print(response)