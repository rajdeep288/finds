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
        col_names = list(df.columns[:-1])
    except:
        col_names = ["Time", "Weather", "Temperature", "Company", "Humidity", "Wind"]
    
    # Use Blocks API for vertical layout + force light/white theme
    with gr.Blocks(theme=gr.themes.Soft(), js="() => { document.querySelector('body').classList.remove('dark'); }") as app:
        gr.Markdown("# FIND-S Algorithm Predictor")
        gr.Markdown("A simple web application indicating whether the particular conditions match the trained FIND-S learned hypothesis.")
        
        input_boxes = []
        for col in col_names:
            tb = gr.Textbox(label=col, placeholder=f"Enter {col}")
            input_boxes.append(tb)
        
        submit_btn = gr.Button("Submit", variant="primary")
        clear_btn = gr.Button("Clear")
        
        output_box = gr.Textbox(label="Prediction (Will Enjoy Sport?)")
        
        submit_btn.click(fn=predict, inputs=input_boxes, outputs=output_box)
        clear_btn.click(fn=lambda: [""] * (len(col_names) + 1), inputs=None, outputs=input_boxes + [output_box])
    
    return app

if __name__ == "__main__":
    import os
    demo = create_app()
    # Leaving launch parameters empty allows Hugging Face to launch cleanly, 
    # but strictly setting 0.0.0.0 and PORT prevents Render from timing out
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
