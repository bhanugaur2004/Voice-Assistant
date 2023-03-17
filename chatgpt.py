import openai

openai.api_key="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"

model_engine = "text-davinci-003"
prompt = "Tips to win an coding hackathon"

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n =1,
    stop = None,
    temperature = 0.5,
)

response = completion.choices[0].text
print(response)