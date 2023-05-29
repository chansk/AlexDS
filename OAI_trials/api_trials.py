
# %% 
import openai
openai.api_key = "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"
# %% 
#returns a list of all OpenAI models
models = openai.Model.list()
# %% 
print(models)

# %% 
# converts the list of OpenAI models to a Pandas DataFrame
import pandas as pd
data = pd.DataFrame(models["data"])
data.head(20)

# %% 
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
# %% 
response['choices'][0]['message']['content']
# %%
