import pysrt
from moviepy.editor import VideoFileClip
from flask import jsonify

def search_keyword_in_videos(keyword, video_files, srt_files):
    keyword_timestamps = {}

    # Search for the keyword in each SRT file
    for srt_file in srt_files:
        subs = pysrt.open(srt_file)
        for sub in subs:
            if keyword.lower() in sub.text.lower():
                if srt_file not in keyword_timestamps:
                    keyword_timestamps[srt_file] = []
                keyword_timestamps[srt_file].append(sub.start.to_time())

    results = {}
    # Open the videos at the timestamps where the keyword occurs
    for video_file, timestamps in keyword_timestamps.items():
        # here u r printing instead u need to send(return these) it to server.py
        # print(f"Video File: {video_file}, Timestamps: {timestamps}")
        # list1_str = ', '.join(map(str, video_file))
        # list2_str = ', '.join(map(str, timestamps))

        # # Concatenate the strings with a separator (e.g., newline)
        # combined_str = list1_str + '\n' + list2_str
        # # t="Video File:"+video_file+ "Timestamps:"+timestamps
        # for timestamp in timestamps:
        #     # Skip opening SRT files as video files                     
        #     if video_file.endswith('.srt'):
        #         continue
        #     video_clip = VideoFileClip(video_file)
        #     # Seek to the timestamp where the keyword occurs
        #     video_clip = video_clip.subclip(t_start=timestamp.total_seconds())
        #     video_clip.preview()
        # return combined_str
        timestamps_str = [str(timestamp) for timestamp in timestamps]
        results[video_file] = timestamps_str

    return results

if __name__ == "__main__":
    keyword = input("Enter keyword to search: ")
    # Provide paths to your video and SRT files
    video_files = ["C:/Users/91990/OneDrive/Desktop/Project/videos/v001.mp4"]  # Adjust the SRT file path
    srt_files = ["C:/Users/91990/OneDrive/Desktop/Project/videos/v001.srt"]  # Remove the SRT file from video_files
    results = search_keyword_in_videos(keyword, video_files, srt_files)
    print(results)