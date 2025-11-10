import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Step 1: Call the API
        response = requests.get(url)
        response.raise_for_status()  # Raises error for bad response (4xx, 5xx)
        
        # Step 2: Parse JSON data
        users = response.json()
        if not users:
            print("No users found!")
            return

        # Step 3: Loop through each user
        for i, user in enumerate(users, start=1):
            name = user.get('name', 'N/A')
            username = user.get('username', 'N/A')
            email = user.get('email', 'N/A')
            city = user.get('address', {}).get('city', 'N/A')

            # BONUS: Print only if city starts with 'S'
            if city.lower().startswith('s'):
                print(f"User {i}:")
                print(f"  Name: {name}")
                print(f"  Username: {username}")
                print(f"  Email: {email}")
                print(f"  City: {city}")
                print("-" * 25)

    except requests.exceptions.RequestException as e:
        print("Error fetching data from API:", e)

if __name__ == "__main__":
    fetch_users()
    