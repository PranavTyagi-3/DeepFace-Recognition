# Face Recognition Web App Documentation

## Overview

This Flask-based web application provides functionality for registering and recognizing faces using the DeepFace library. Users can register their faces and later use the application to recognize registered faces from uploaded images.

## Prerequisites

Before using this application, make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- DeepFace
- OpenCV
- Web browser

You can install the required Python libraries by running the following command within your project directory:

```bash
pip install -r requirements.txt
```
## Application Structure

The application consists of the following components:

- `app.py`: The main Flask application script.
- `templates/`: Directory containing HTML templates for rendering web pages.
- `static/`: Directory for storing static files such as uploaded images.

## Configuration

- `app.secret_key`: A secret key used for securing session data.
- `ALLOWED_EXTENSIONS`: A set of allowed file extensions for image uploads.
- `UPLOAD_FOLDER`: Directory to store uploaded images.
- `REGISTER_FOLDER`: Directory to store registered user images.

## Functions

### `allowed_file(filename)`

Checks if the provided filename has an allowed file extension.

### `new(user_id)`

Checks if a user with the given `user_id` is new (not registered) based on the presence of their image in the `REGISTER_FOLDER`.

### `index()`

Renders the application's homepage (index.html).

### `register()`

- Renders the registration page (register.html).
- Handles user registration, including image upload and face detection.
- Validates user input, checks for duplicate user IDs, and verifies image files.

### `recognition()`

- Renders the recognition page (recognize.html).
- Handles face recognition for uploaded images.
- Uses the `recognize()` function to compare uploaded images with registered user images.

### `recognize(uploaded_file)`

- Compares the uploaded image with registered user images to verify identity.
- Utilizes DeepFace for face verification using the Facenet model.

## Usage

1. Start the Flask application by running `python app.py`.

2. Access the application in your web browser at `http://localhost:5000`.

3. Register new users by uploading their images on the registration page.

4. Recognize users by uploading images on the recognition page.

## Error Handling

- The application handles various error scenarios, such as file type validation, duplicate user IDs, and unsuccessful face recognition.

## Dependencies

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [DeepFace](https://github.com/serengil/deepface)
- [OpenCV](https://opencv.org/)

## Contributions

Contributions to the project are welcome. If you encounter issues or have suggestions, please open an issue or submit a pull request on the [GitHub repository](https://github.com/PranavTyagi-3/DeepFace-Recognition).


## Acknowledgments

- This application uses the DeepFace library for face recognition.
- Special thanks to the Flask and Python communities for their contributions to open-source software.
