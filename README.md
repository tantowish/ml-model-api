# Dental Classification Deep Learning API

This repository contains a deep learning model for dental classification, developed using Teachable Machine by Google and deployed as an API using Python with the Flask library. The API is designed to classify dental images into different categories.

## Key Features

- **Teachable Machine Integration**: Utilizes Teachable Machine, a platform by Google, for training the deep learning model with dental images.
- **Deep Learning Model**: The core of the project, featuring a neural network trained on a dataset of dental images to accurately classify various dental conditions.
- **Flask API**: Utilizes Flask, a lightweight web framework for Python, to deploy the trained model as an API.
- **RESTful Interface**: Provides a RESTful API interface where users can send dental images via HTTP requests and receive classification predictions.
- **Scalable and Accessible**: Being an API, it allows easy integration into various applications and can be scaled to handle multiple requests concurrently.

## Usage

1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in the requirements.txt file.
3. Run the Flask application using the command `python app.py`.
4. Send HTTP POST requests with dental images to the API endpoint to receive classification predictions.

## Credits

This project was developed by Gatau Tanya ChatGPT Team for the Google Solution Challenge, with the aim of providing an accessible API for automated dental image classification.

For more information, feel free to contact the project maintainer(s).
