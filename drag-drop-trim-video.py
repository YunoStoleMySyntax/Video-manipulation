import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def trim_video(input_file, start_time, end_time, output_file):
    try:
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
        print("Trimmed video successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

def get_video_duration(input_file):
    try:
        clip = VideoFileClip(input_file)
        duration = clip.duration
        return duration

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: drag_and_drop_trim.py <input_video>")
        sys.exit(1)

    input_file = sys.argv[1]

    duration = get_video_duration(input_file)
    if duration is not None:
        print(f"Video duration: {duration} seconds")

    start_time = float(input("Enter the start time (in seconds): "))
    end_time = float(input("Enter the end time (in seconds): "))

    output_file = input_file.replace('.mp4', '_trimmed.mp4')

    trim_video(input_file, start_time, end_time, output_file)

if __name__ == "__main__":
    main()

