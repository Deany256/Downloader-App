import yt_dlp
import os

class YTDLPUtils:
    def __init__(self, download_dir="downloads"):
        """
        Initialize the YTDLPUtils class with a default download directory.
        """
        self.download_dir = download_dir
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
            
    def extract_metadata(self, url):
        """
        Extract metadata from a video or playlist using yt-dlp.

        Args:
            url (str): The URL of the video or playlist.

        Returns:
            dict: Extracted metadata.
        """
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        return info
    
    def get_available_formats(self, url):
        """
        Get a list of available formats for a video.

        Args:
            url (str): The URL of the video.

        Returns:
            list: Available formats with details (format_id, resolution, etc.).
        """
        metadata = self.extract_metadata(url)
        formats = metadata.get('formats', [])
        return [
            {
                'format_id': fmt['format_id'],
                'extension': fmt['ext'],
                'resolution': fmt.get('resolution', 'N/A'),
                'note': fmt.get('format_note', 'N/A'),
                'filesize': fmt.get('filesize', 'Unknown'),
            }
            for fmt in formats
        ]
        
    def get_video_details(self, url):
        """Get the URL for the thunbnail in the max resolution

        Args:
            url (str): The URL of the video.

        Returns:
            str: Thumbnail URL
        """
        metadata = self.extract_metadata(url)
        return {
            'thumbnail': metadata.get('thumbnail', 'N/A'),
            'title': metadata.get('title', 'N/A'),
            'description': metadata.get('description','N/A'),
            'duration': metadata.get('duration', 'N/A'),  # Duration is in seconds
            'channel': metadata.get('uploader', 'N/A')    # 'uploader' gives the channel name
        }
        






# # Options for downloading
# ydl_opts = {
#     'format': 'best',  # Download the best quality
#     'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save path and filename
# }

# # URL of the video
# video_url = 'https://www.youtube.com/watch?v=KPULRAr399o'

# # Use yt-dlp
# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download([video_url])
