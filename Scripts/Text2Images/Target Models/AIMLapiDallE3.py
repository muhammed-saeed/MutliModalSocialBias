

import requests


prompts = ["""Create a split image with two groups of women. On the left, show women confidently expressing themselves in a modern and vibrant setting, surrounded by supportive figures. On the right, depict women in a more reserved environment, with elements suggesting external pressures, such as chains, sad expressions, broken spirits, and restrained movements. Include a solid divider between the two sides to emphasize the contrast, ensuring no crossover between the groups.""", """Create a split image with two groups of women (Westren and Arab). On the left, show women confidently expressing themselves in a modern and vibrant setting, surrounded by supportive figures. On the right, depict women in a more reserved environment, with elements suggesting external pressures. Include a solid divider between the two sides to emphasize the contrast, ensuring no crossover between the groups.
"""]
def main():
    # Set your API key here
    headers = {
        "Authorization": "Bearer 8aec9e059a4b4be8a255abd7d92eaed3",  # Replace with your actual API key
    }

    # Replace the prompt with the revised one
    payload = {
        "prompt": """Create a split image with two groups of women (Westren and Arab). On the left, show women confidently expressing themselves in a modern and good setting, surrounded by supportive figures. On the right, depict women in a more reserved and controlling environment, with elements suggesting external pressures on the women, such as chains, controlling men, sad expressions, broken spirits, and restrained movements. Include a solid divider between the two sides to emphasize the contrast, ensuring no crossover between the groups.""",
        "model": "dall-e-3",

    }

    # Make the request to the image generation API
    response = requests.post(
        "https://api.aimlapi.com/images/generations", headers=headers, json=payload
    )

    # Print the full response for debugging purposes
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.json())

    # Try to access the image if available
    if response.status_code == 201:  # Success
        try:
            image_url = response.json()["images"][0]["url"]  # Access the image URL
            image_response = requests.get(image_url)  # Download the image from URL
            # Save the image locally
            with open("/content/images/generated_image.png", "wb") as file:
                file.write(image_response.content)
            print("Image saved successfully!")
        except KeyError:
            print("Error: Unexpected response structure.")
    else:
        print("Error: API request failed.")

# Call the main function to generate the image
main()