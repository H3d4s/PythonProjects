from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytube import YouTube

# Initialize the WebDriver (specify the path to your WebDriver executable)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Step 1: Login with Selenium
def login_to_youtube():
    # Open YouTube's login page
    driver.get("https://www.youtube.com")

    # Find the "Sign In" button and click it
    sign_in_button = driver.find_element_by_link_text("Sign in")
    sign_in_button.click()

    # Enter your YouTube account credentials
    email_input = driver.find_element_by_id("identifierId")
    email_input.send_keys("your_email@gmail.com")
    email_input.send_keys(Keys.RETURN)

    # Enter your password and complete the login process
    password_input = driver.find_element_by_name("password")
    password_input.send_keys("your_password")
    password_input.send_keys(Keys.RETURN)

# Step 2: After successful login, get the URL of the video you want to download
def get_video_url():
    # Navigate to the video you want to download
    driver.get("https://www.youtube.com/watch?v=S0z5JmpQ--w")

    # Get the current URL, which will be the URL of the video page
    video_url = driver.current_url
    return video_url

# Step 3: Use Pytube to download the video
def download_video(video_url):
    yt = YouTube(video_url)

    # Print video details.
    print("Video Title:", yt.title)
    print("Video Length (seconds):", yt.length)

    # Choose the stream with the desired resolution and format.
    stream = yt.streams.filter(res="720p", file_extension="mp4").first()

    # Download the video to the specified directory.
    stream.download(output_path="C:\\Users\\ACER\\Downloads")  # Update with your desired download path.

# Main program
if __name__ == "__main__":
    login_to_youtube()
    video_url = get_video_url()
    download_video(video_url)

# Don't forget to close the browser when you're done
driver.quit()
