import wikipedia
from rapidfuzz import process
import sys

def fetch_company_info(company_name):
    try:
        search_results = wikipedia.search(company_name)
        if not search_results:
            return {"Error": "No search results found on Wikipedia."}
        
        match = process.extractOne(company_name, search_results)
        if not match:
            return {"Error": "No sufficiently close match found for the given input."}

        best_match, score = match[0], match[1]
        if score < 70:
            return {"Error": "No sufficiently close match found for the given input."}
        
        page = wikipedia.page(best_match)
        return {
            "Title": page.title,
            "Summary": wikipedia.summary(best_match, sentences=3),
            "URL": page.url
        }
    except wikipedia.DisambiguationError as e:
        return {"Error": f"Disambiguation Error: {e.options}"}
    except wikipedia.PageError:
        return {"Error": "Page not found"}
    except Exception as e:
        return {"Error": str(e)}

def main():
    if len(sys.argv) < 2:
        print("Usage: python scraper.py '<company_name>'")
        sys.exit(1)
    company_name = sys.argv[1]
    print(f"Fetching information for company: {company_name}")
    company_info = fetch_company_info(company_name)
    for key, value in company_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
