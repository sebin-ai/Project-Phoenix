import gradio as gr

def greet():
    return "🚀 Welcome to Project Phoenix!\n\nYour AI Video Generator is officially running."

app = gr.Interface(
    fn=greet,
    inputs=None,
    outputs="text",
    title="Project Phoenix",
    description="Create amazing AI-powered videos with just a few clicks."
)

app.launch()