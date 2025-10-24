import requests
import json

def travel_itinerary_bot_llama():
    """Command-line AI Travel Itinerary Generator (Local LLaMA Version)"""
    print("🌍 Welcome to the LLaMA Travel Itinerary Generator!\n")

    # 收集用户输入
    days = input("How many days will you travel? ")
    location = input("Where is your destination city? ")
    age = input("Enter your age: ")

    # 构造 prompt
    prompt = f"""
    You are a professional travel planner.
    Create a detailed travel itinerary based on these details:

    - Duration: {days} days
    - Destination: {location}
    - Traveler age: {age}

    Provide a structured plan:
    For each day, list up to 3 recommended activities.
    Each activity should include:
    - Name of the place
    - Address (if known)
    - Short description (why it's recommended)
    """

    # 调用本地 Ollama API
    try:
        print("\n🤖 Generating itinerary using LLaMA model...\n")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1",  # 你本地下载的模型名
                "prompt": prompt,
                "stream": False
            }
        )

        if response.status_code == 200:
            data = response.json()
            print("🧭 Your Personalized Travel Itinerary:\n")
            print(data["response"])
        else:
            print("⚠️ Ollama API returned an error:", response.text)

    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Make sure Ollama is running locally.")
        print("You can start it by launching the Ollama app or running: ollama serve")

    except Exception as e:
        print("⚠️ Unexpected error:", e)


if __name__ == "__main__":
    travel_itinerary_bot_llama()

