import os
import google.generativeai as genai 

genai.configure(api_key="AIzaSyDf_wCtAFB3iwerFs1ogCz19GEUBDtA4YA")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
def GenerateResponse(input_text):
     response = model.generate_content([
     "answer all questions as possible",
     "input: who are you?",
     "output: I'm the School Help Desk",
     "input: what all you can do?",
     "output: i can help by answering you inqueries",
     f"input: {input_text}",
     "output: ",
     ])
     return response.text


