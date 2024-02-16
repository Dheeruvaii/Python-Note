import requests


def save_image_from_url(url, filename):

    response = requests.get(url)    

    if response.status_code == 200:

        with open(filename, 'wb') as file:

            file.write(response.content)

        print(f"Image saved as {filename}")

    else:

        print("Failed to download the image")

# URL of the image

image_url = "https://example.com/image.jpg"

# Name for the saved image file

output_filename = "saved_image.jpg"

# Save the image

save_image_from_url(image_url, output_filename)