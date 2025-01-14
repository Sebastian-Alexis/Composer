from together import Together
import re

client = Together()

def generate_email(template, company_summary):
    """
    Generate a professional email using Together API based on the provided template
    and company summary.

    Args:
        template (str): The email template with placeholders.
        company_summary (str): The company summary to fill in the template.

    Returns:
        str: The generated email text.
    """
    prompt = (
        "You are a professional email generator. "
        "Using the provided email template and company summary, generate a polished email. "
        "Replace placeholders like '{{Company Summary}}' with the provided company summary. "
        "Ensure the email is professional and well-structured, ready to be sent. "
        "Do not include any headers or extra information; only return the email text."
    )
    
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Email Template: {template}"},
                {"role": "user", "content": f"Company Summary: {company_summary}"}
            ],
        )
        response = completion.choices[0].message.content

        # Clean up response formatting
        email_text = re.sub(r"^\**|\**$", "", response).strip()
        email_text = re.sub(r"\s{2,}", " ", email_text)  # Collapse multiple spaces into one

        return email_text
    except Exception as e:
        print(f"Error using Together API: {e}")
        return "An error occurred while generating the email."
























































