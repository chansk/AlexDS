
# %% 
import openai
import os
import pandas as pd
#open.api_key = os.environ["OPENAI_API_KEY"]
open.api_key = os.environ.get('OPENAI_API_KEY')

#openai.api_key = "s"
# %% This is working now but would much rather have it stored in environment long term than name to path
with open('/Users/alexanderchansky/Downloads/GPT_API_key.txt', 'r') as file:
    api_key = file.read().strip()

# Set the API key
openai.api_key = api_key
# %% 
#returns a list of all OpenAI models
models = openai.Model.list()
print(models)

# converts the list of OpenAI models to a Pandas DataFrame
data = pd.DataFrame(models["data"])
data.head(20)

# %% GPT 3.5 seems overall best, use that or 4.0 in production
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

# %% GPT 3.5 seems overall best, use that or 4.0 in production
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Explain the following like I'm 5 years old: "},
        {"role": "user", "content": "What is the big bang?"}
    ],
  max_tokens=100
)
# %% 
response['choices'][0]['message']['content']

# Ada is cheapest, but only completes sentences, so cannot use for testing
# %% A
response_ada = openai.Completion.create(
  model="text-ada-001",
  prompt="Explain the following like I'm 5 years old: What is the big bang?",
  max_tokens=100,
  temperature=0
)
# %%
response_ada['choices'][0]['text']
# Still puts out "\n\n" at beginning of text but close enough
# %% testing it with string input
my_string = "What is the big bang?"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "Explain the following like I'm 5 years old: "},
        {"role": "user", "content": my_string}
    ],
  max_tokens=100
)
# %% 
response['choices'][0]['message']['content']

# %% 
# Generate an image
response = openai.Image.create(
    prompt="avocado attacking a dog",
    model="image-alpha-001",
    size="1024x1024",
    response_format="url"
)

# %%
print(response["data"][0]["url"])
# %%
