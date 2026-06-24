from transformers import pipeline
import gradio as gr

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)
def generate_video(prompt):

    result = generator(
        prompt,
        max_length=80,
        num_return_sequences=1
    )

    ai_story = result[0]["generated_text"]

    return f"""
🎬 Video Generation Started

📝 Video Idea:
{prompt}

📖 AI Script:
{ai_story}

🎥 Scene 1:
Introduction to the story.

🎥 Scene 2:
The main action unfolds.

🎥 Scene 3:
A dramatic conclusion leaves viewers amazed.

🎨 Suggested Style:
Cinematic, Ultra HD, Realistic

⏳ Status:
Ready for AI image generation
"""
    return f"""
🎬 Video Generation Started

📝 Idea: {prompt}

📖 Script:
Once upon a time, {prompt.lower()}.

🎥 Scenes:
1. Opening cinematic shot
2. Main action sequence
3. Dramatic ending

⏳ Status: Ready for AI video creation
"""

app = gr.Interface(
    fn=generate_video,
    inputs=gr.Textbox(label="Video Idea", placeholder="Enter your video idea..."),
    outputs="text",
    title="Project Phoenix",
    description="Create amazing AI-powered videos with just a few clicks."
)

app.launch()