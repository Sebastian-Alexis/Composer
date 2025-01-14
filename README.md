# Composer: Wikipedia Summarizer and Email Generator

Composer is a Flask-based web application that allows users to fetch summaries from Wikipedia and generate professional emails using the Together API. 

## Features
- **Fetch Wikipedia Summary**: Enter a Wikipedia URL to retrieve a concise summary of the page.
- **Generate Professional Emails**: Provide an email template and company summary to generate a polished email using the Together API.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/composer.git
   cd composer
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   - Set the `TOGETHER_API_KEY` for the Together API.
     ```bash
     export TOGETHER_API_KEY=your_api_key  # On Windows: set TOGETHER_API_KEY=your_api_key
     ```

## Usage

1. **Run the Flask App**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   - Open a browser and navigate to: `http://127.0.0.1:5000`.

3. **Fetch a Wikipedia Summary**:
   - Enter a Wikipedia URL in the "Company Information" field and click **Fetch Summary**.
   - The summary will be displayed in the "Company Summary" section.

4. **Generate an Email**:
   - Provide an email template in the "Email Template" field.
   - Click **Generate Email** to create a professional email based on the template and summary.

## Project Structure

```plaintext
composer/
│
├── app.py                # Flask application
├── scraper.py            # Wikipedia summarizer logic
├── togetherapi.py        # Email generation logic using Together API
├── templates/
│   └── base.html         # Base HTML template
│   └── index.html        # Main application UI
├── static/               # Static files (CSS, JS, images)
├── .venv/                # Virtual environment (ignored in .gitignore)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Technologies Used

- **Backend**: Flask
- **Frontend**: TailwindCSS, DaisyUI
- **APIs**: 
  - Wikipedia API for summaries.
  - Together API for email generation.

## Environment Variables

| Variable          | Description                              |
|--------------------|------------------------------------------|
| `TOGETHER_API_KEY` | API key for the Together API integration |

## Example API Calls

- **Fetch Wikipedia Summary**:
   ```bash
   POST /scrape
   Content-Type: application/json

   {
     "wikipedia_url": "https://en.wikipedia.org/wiki/Tesla,_Inc."
   }
   ```

- **Generate Email**:
   ```bash
   POST /generate-email
   Content-Type: application/json

   {
     "template": "Dear {{Name}},\n\nWe are pleased to announce...",
     "company_summary": "Tesla is a leading electric vehicle company..."
   }
   ```

## License
This project is licensed under the MIT License.
