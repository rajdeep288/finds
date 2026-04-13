# Deployment Guide

This repository contains the Find-S Algorithm implementation and a Web Application (Gradio) to serve predictions based on the learned hypothesis. The web application defaults to the dynamically trained parameters.

## Prerequisites
1. First, make sure you run `find_s.py` locally to generate the `hypothesis.json` model file:
   ```bash
   python3 find_s.py
   ```
2. Install the requirements locally if you want to test the app:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

Below are instructions on how to deploy this on Hugging Face Spaces and Render.

---

## 1. Deploying on Hugging Face Spaces

Hugging Face Spaces natively supports Gradio!

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and create a new Space.
2. Select **Gradio** as your Space SDK.
3. Choose the Space hardware (the free tier is 100% fine for this project).
4. Once your Space is generated, upload the following files to your Space's repository:
   - `app.py`
   - `requirements.txt`
   - `hypothesis.json` (the exact learned hypothesis produced by your script)
   - `EnjoySport.csv`
5. The application will automatically build and launch!

---

## 2. Deploying on Render

Render enables you to easily deploy Python Web Services.

1. Push your code to a GitHub/Gitlab repository (including `app.py`, `requirements.txt`, `hypothesis.json`, and `EnjoySport.csv`).
2. Go to the [Render Dashboard](https://dashboard.render.com/) and click on **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Set up the details for your Web Service:
   - **Name**: e.g. `find-s-predictor`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Scroll down to **Advanced** and add an Environment Variable if you wish (usually none are strictly necessary for Gradio, though it is deploying to port 10000, which Render maps dynamically). Gradio will read the `0.0.0.0` port setup natively!
6. Click **Create Web Service**. Wait for the build and deployment process to finish (which usually takes a couple of minutes). Once deployed, Render will provide a public URL for your web app.
