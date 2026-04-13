import gradio as gr
import json
import pandas as pd
import numpy as np

# Load hypothesis
def load_hypothesis():
    try:
        with open('hypothesis.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return ["?"] * 6 # Default generic hypothesis if file is missing

def predict(*features):
    hypothesis = load_hypothesis()
    
    # Check if features match hypothesis
    for h, f in zip(hypothesis, features):
        if h != '?' and h.strip().lower() != str(f).strip().lower():
            return "No (Does not Match Hypothesis)"
            
    return "Yes (Matches Hypothesis)"

def create_app():
    # Attempt to load columns dynamically from CSV or fallback to defaults
    try:
        df = pd.read_csv('EnjoySport.csv')
        inputs = [gr.Textbox(label=col, placeholder=f"Enter {col}") for col in df.columns[:-1]]
    except:
        inputs = [
            gr.Textbox(label="Time (e.g. Morning, Evening)"),
            gr.Textbox(label="Weather (e.g. Sunny, Rainy)"),
            gr.Textbox(label="Temperature (e.g. Warm, Cold)"),
            gr.Textbox(label="Company (e.g. Yes, No)"),
            gr.Textbox(label="Humidity (e.g. Mild, Normal, High)"),
            gr.Textbox(label="Wind (e.g. Strong, Normal)")
        ]
    
    app = gr.Interface(
        fn=predict,
        inputs=inputs,
        outputs=gr.Textbox(label="Prediction (Will Enjoy Sport?)"),
        title="FIND-S Algorithm Predictor",
        description="A simple web application indicating whether the particular conditions match the trained FIND-S learned hypothesis."
    )
    return app

if __name__ == "__main__":
    import os
    demo = create_app()
    # Leaving launch parameters empty allows Hugging Face to launch cleanly, 
    # but strictly setting 0.0.0.0 and PORT prevents Render from timing out
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
