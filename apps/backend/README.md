# Backend - Flask API

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment variables:
```bash
cp .env.example .env
```

4. Run the application:
```bash
python app.py
```

## Nx Commands

From the root directory:

- `nx serve backend` - Start the Flask server
- `nx install backend` - Install Python dependencies
- `nx test backend` - Run tests