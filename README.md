# Quizer - Quiz App

This repository contains the Django project Quizer, which includes a form application that includes quiz backend apis.

## Description
Quizer is a quiz application built using Django. It allows users to create and take quizzes.

## Project Structure
- Static HTML files are located in the `quizer/static/quizer` folder.

## CORS Configuration
Currently, Cross-Origin Resource Sharing (CORS) is set to accept requests from `localhost:8080`.

## Installation
1. Create a Python virtual environment (if not already present):
    - On Linux/Mac: `python3 -m venv venv`
    - On Windows: `python -m venv venv`
2. Activate the virtual environment:
    - On Linux/Mac: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`
3. Install project dependencies from requirements.txt:
    ```
    pip install -r requirements.txt
    ```

## Running the Django Project
1. Navigate to the project directory:
    ```
    cd quizer
    ```
2. Run the Django development server:
    ```
    python manage.py runserver
    ```
3. Optionally, you can use the "serve" package to host static files. If not installed, you can install it using npm:
    ```
    npm install -g serve
    ```
4. Start the local server to serve static files:
    ```
    serve -s static
    ```
5. Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Documentation
For API documentation on the form application, you can use Swapper. Access it at [localhost:8000/form/api/docs](http://localhost:8000/form/api/docs).
