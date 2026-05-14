import openai
import os
#from gtts import gTTS
import setup

conversation_history = [f"从现在开始，你需要扮演下面的角色来回答我的任何后续问题({setup.CHAR1}，你需要扮演的更加自然，就像和我再聊天闲谈一样，下面是我们的聊天记录，你需要对最新的问题作出回应(请将输出控制在150字符内):"]

def respond():
    # Set proxy if needed
    os.environ["http_proxy"] = "http://localhost:7890"
    os.environ["https_proxy"] = "http://localhost:7890"
    audio = r'.\audioflow\output.mp3'

    # Initialize OpenAI client
    client = openai.OpenAI(api_key='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')

    # Transcribe audio to text
    if os.path.exists(audio):
        with open(audio, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )

        # 将新的转录添加到对话历史
        global conversation_history
        conversation_history.append(transcript)
        os.remove(audio)

        # 将整个对话历史发送给 GPT-3
        full_prompt = "\n".join(conversation_history)
        print(full_prompt)
        response = client.completions.create(
            model="text-davinci-003",
            prompt=full_prompt,
            max_tokens= 300
        )

        """
        # Convert GPT-3 response to audio using gTTS
        tts = gTTS(response['choices'][0]['text'])
        tts.save("response.mp3")
        """
        print(response)
        conversation_history.append(response.choices[0].text)

        # Generate speech using OpenAI's TTS model
        tts_response = client.audio.speech.create(
          model="tts-1",
          voice="alloy",
          input=response.choices[0].text
        )

        # Save the audio stream to a file
        tts_response.stream_to_file(r".\examples\driven_audio\response.mp3")

if __name__ == '__main__':
    respond()