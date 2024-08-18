# app/Dockerfile

# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install JupyterLab
RUN pip3 install jupyterlab streamlit

# Expose the ports for Streamlit and JupyterLab
EXPOSE 8501 8888

# Healthcheck for Streamlit
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Start Streamlit and JupyterLab services
CMD streamlit run app.py & jupyter lab --ip=0.0.0.0 --allow-root
