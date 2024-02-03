
# DrNiceFellow's Simple Chat Console UI

![Screenshot](/assets/screenshot.png)

This is a simple chat console UI developed by Dr. Nicefellow. It is designed to provide a user-friendly interface for interacting with a chatbot in a console environment. The backend engine is powered by OpenAI API, and the backend LLM should support the Llama Chat/Mistral Instruct prompt template. It is tested with Tabbyapi.

## Features

- User-friendly console interface
- Backend engine powered by OpenAI API
- Support for Llama Chat/Mistral Instruct prompt template

## Requirements

- Python
- Requests
- Colorama
- PyYAML

## Installation

1. Clone the repository
2. Start the backend server and obtain the API key and host address.
3. Install the required packages using pip.
4. Create a `config.yml` file with the example `example.config.yml` and set the OpenAI API key.
5. Run the application:
   ```
   python main_console.py
   ```

## Usage

Run the script in your console. You can start chatting with the bot by typing your message and pressing the "Enter" key. 

- To exit the chat, type `exit` and press "Enter".
- To clear the chat history, type `clear` and press "Enter".

## TODO

- Add support for other chat formats
- Add function calling

## License

This project is licensed under the terms of the Apache 2.0 License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
