import google.generativeai as genai


key = '' #insert key here
genai.configure(api_key=key)

safety_settings={
    'HATE': 'BLOCK_SOME',
    'HARASSMENT': 'BLOCK_SOME',
    'SEXUAL' : 'BLOCK_SOME',
    'DANGEROUS' : 'BLOCK_SOME'
}

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5
}

model = genai.GenerativeModel('gemini-pro',
                            generation_config=generation_config,
                            safety_settings=safety_settings)
## Can be used from here on for zero-shot answer or train few-shot
## Example
## response = model.generate_content("In one sentence, explain how a computer works to a young child.")
## print(response.text)

chat = model.start_chat(history=[]) #clear history/zero-shooting


## chat bot basic model
talk_box = input('Your turn:')
i=0 
chat_max_m = 10
while talk_box != 'FIM' or i>=chat_max_m:
    response = chat.send_message(talk_box)
    print(f'Answer: {response.text}')
    talk_box = input('Your turn:')
    i+=1