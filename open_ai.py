import tkinter as tk
import os
import openai

def aichat():
    os.system("espeak-ng 'get ready to chat with AI...'")
    mykey="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"
    openai.api_key = mykey

    def chat_with_gpt(prompt,Messages):
        res02=openai.ChatCompletion.create(
                model= "gpt-3.5-turbo",max_tokens=100,
                messages= [
                    {"role": "system", "content":prompt},
                    {"role": "user", "content":Messages }
                    ]
                ) 
        return (res02.choices[0].message.content)
    def send_message():
        user_input = user_input_text.get("1.0", "end").strip()
        chat_log.insert(tk.END, f"You: {user_input}\n")
        user_input_text.delete("1.0", tk.END)

        prompt = chat_log.get("1.0", tk.END).strip() + f"\nUser: {user_input}\nChatGPT:"
        chatbot_response = chat_with_gpt(user_input,prompt)

        chat_log.insert(tk.END, f" {chatbot_response}\n")
        chat_log.see(tk.END)

    window = tk.Tk()
    window.title("Chatbot App")

    chat_log = tk.Text(window, height=30, width=150)
    chat_log.pack()

    user_input_text = tk.Text(window, height=3, width=100)
    user_input_text.pack()

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack()

    window.mainloop()
