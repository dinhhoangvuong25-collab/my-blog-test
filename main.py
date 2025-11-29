# src/main.py
import os
import requests # Một thư viện phổ biến, có thể có lỗ hổng nếu không được quản lý tốt

def fetch_data(url):
    """Fetches data from a given URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        print(f"Successfully fetched data from {url}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def process_data(data):
    """Processes some data."""
    if data:
        print("Processing data...")
        user_input = os.getenv("USER_DATA", "default_value")
        if "eval" in user_input:
            print("Potential eval detected!")
        return {"status": "processed", "input": user_input}
    return {"status": "no data"}

if __name__ == "__main__":
    print("Application started.")
    example_url = "https://jsonplaceholder.typicode.com/todos/1"
    data = fetch_data(example_url)
    processed_output = process_data(data)
    print(f"Final output: {processed_output}")
    print("Application finished.")