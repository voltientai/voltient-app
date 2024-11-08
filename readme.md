# Voltient

A cloud-based application for processing and managing data workflows.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/voltient.git
cd voltient
```

2. Create and activate virtual environment:

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Local Development

### Running the Application

Standard Python:
```bash
python app.py
```

With Streamlit:
```bash
streamlit run app.py
```

### Configuration
1. Update the environment variables in `.env` with your settings:
```
ANTHROPIC_API_KEY=your-key-goes-here
```

## Development Commands

### Virtual Environment Management
```bash
# Create new environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Mac
.\venv\Scripts\activate   # Windows

# Deactivate environment
deactivate

# Reset environment
deactivate
rm -rf venv
```

### Dependencies
```bash
# Install requirements
pip install -r requirements.txt

# Update requirements file
pip freeze > requirements.txt
```

## Using Aider AI for Development
```bash
# Set Anthropic Key for using Claude 3.5 Sonnet
export ANTHROPIC_API_KEY=your-key-goes-here

# Run Aider CLI tools with app.py for context
aider app.py
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License