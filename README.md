## Flask Weather App

This is a simple Flask application that fetches weather data from the OpenWeatherMap API based on user input (city name) and displays the weather information.

## Features

- Allows users to input a city name and retrieve weather information.
- Displays temperature, description, and weather icon for the specified city.

## Prerequisites

Before running this application, you need to obtain an API key from OpenWeatherMap. You can sign up and get your API key [here](https://home.openweathermap.org/users/sign_up).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/flask-weather-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-weather-app
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory of the project and add your OpenWeatherMap API key:

   ```
   OPENWEATHERMAP_API_KEY=YOUR_OPENWEATHERMAP_API_KEY
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).
3. Enter a city name in the input field and click "Get Weather" to retrieve weather information for that city.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add my feature'`).
5. Push to the branch (`git push origin feature/my-feature`).
6. Create a new pull request.

