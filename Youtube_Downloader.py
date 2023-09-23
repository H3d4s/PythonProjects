from pytube import YouTube

# Replace the URL below with the URL of the YouTube video you want to download.
video_url = "https://www.youtube.com/watch?v=S0z5JmpQ--w"

# Replace this with the directory path where you want to save the downloaded video.
download_path = "C:\\Users\\ACER\\Downloads"

# Create a YouTube object.
yt = YouTube(video_url)

# Print video details.
print("Video Title:", yt.title)
print("Video Length (seconds):", yt.length)

# Choose the stream with the desired resolution and format.
# For example, to download the highest resolution available, use:
# stream = yt.streams.get_highest_resolution()

# To download a specific resolution and format, you can specify it like this:
stream = yt.streams.filter(res="720p", file_extension="mp4").first()

# Download the video to the specified directory.
stream.download(output_path=download_path)

print("Download complete.")
