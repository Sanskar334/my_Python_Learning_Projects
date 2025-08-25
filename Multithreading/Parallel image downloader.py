# importing threads for parallel downloading images.)
# This is useful when downloading multiple things, this saves time by parallely downloading them.
import threading
# importing requests to get data from the internet. (here we are using it to download images.)
import requests

# This function will download the image from the given URL and save it with a unique name.
def download_image(url, idx): # url here is the image url and idx is the index number of the image.
    # This will get the image from the url.
    response = requests.get(url)
    # This saves the image in a unique file using the index number.
    with open(f"image{idx}.png", "wb") as file: # wb is write binary, used for writing binary files like images.
        # we use .png as the extension for the image file.
        # .content is use to get the content of the image in bytes. That's why we use wb mode to decode the image.
        file.write(response.content)

image_urls = [] # This empty list will hold the image URLs that we want to download.
# I used for loop to take multiple inputs from the user.
for i in range(2):
    u = input(f"Enter the image {i+1}: ")
    image_urls.append(u) # Appending(adding) the user input URL to the image_urls list.

# As already mentioned above url here is the image url and idx is the index number of the image.
for idx, url in enumerate(image_urls):
    # Creating a thread for each image download using Thread function from threading library.
    url1 = threading.Thread(target=download_image, args=(url, idx))
    url1.start() # This will start the thread and call the download_image function with the given URL and index.
        
    url1.join() # This will wait for all threads to complete before exiting the program.

'''This is not considered as a multithrreaded program because we are waiting for each thread to complete before starting the next one.
I think we need to put links in the list to make it a working multithreaded program.'''
'''Put comments on the code to make it more readable.'''
'''As the code is small I dind't focused on creating classes.'''