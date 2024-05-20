# Password Generator

This is a simple Python script that generates passwords based on user-specified difficulty levels. The difficulty levels determine the length and complexity of the generated password.

## Features

- Generates passwords of varying difficulty:
  - **Easy**: Includes lowercase letters and is 8 characters long.
  - **Medium**: Includes lowercase and uppercase letters, and numbers, and is 12 characters long.
  - **Hard**: Includes lowercase and uppercase letters, numbers, and special characters, and is 16 characters long.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository**:
   ```
   git clone https://github.com/singhvijayp/passgen.git
   cd passgen
   ```

2. **Run the Script**:
   ```
   python passgen.py
   ```

3. **Follow the Prompts**:
   - The script will prompt you to select a password difficulty level:
     ```
     Select password difficulty level:
     1. Easy
     2. Medium
     3. Hard
     Enter the number of your choice:
     ```
   - Enter the number corresponding to your choice (1 for Easy, 2 for Medium, 3 for Hard).
   - The script will generate and display a password based on the selected difficulty level.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Acknowledgements

- This script uses the `string` and `random` libraries from Python's standard library.