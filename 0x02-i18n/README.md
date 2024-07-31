# i18n in Flask

This project demonstrates internationalization (i18n) in a Flask web application. The following tasks were completed to achieve this:

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Flask
- Flask-Babel
- pycodestyle 2.5
- pytz

## Tasks

### 0. Basic Flask app

- Created a basic Flask application with a single route that renders a "Welcome to Holberton" title and "Hello world" header.

### 1. Basic Babel setup

- Installed Flask-Babel and set up basic Babel configuration with support for English and French languages.

### 2. Get locale from request

- Added a `get_locale` function to determine the best match for supported languages based on the request headers.

### 3. Parametrize templates

- Used the `_` function to parametrize the templates with message IDs `home_title` and `home_header`.
- Created translation files for English and French.

### 4. Force locale with URL parameter

- Added the ability to force a particular locale by passing the `locale` parameter in the URL.

### 5. Mock logging in

- Mocked a user login system and displayed a welcome message if the user is logged in.

### 6. Use user locale

- Modified `get_locale` to use the user's preferred locale if available.

### 7. Infer appropriate time zone

- Added a `get_timezone` function to determine the best match for supported time zones based on the URL parameter or user settings.

### 8. Display the current time

- Displayed the current time on the home page based on the inferred time zone.

## How to run

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run the desired script using `python3 <script_name>.py`.

## License

This project is licensed under the MIT License.

