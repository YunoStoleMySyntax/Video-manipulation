import os
import sys
import argparse
import fileinput
from moviepy.editor import VideoFileClip
from mutagen import File

def extract_metadata(video_path):
    try:
        video = VideoFileClip(video_path)
        duration = video.duration
        resolution = f"{video.size[0]}x{video.size[1]}"
        codec = video.fps
        return duration, resolution, codec
    except Exception as e:
        print(f"Error extracting video metadata: {str(e)}")
        return None, None, None

def get_existing_metadata(video_path):
    try:
        metadata = File(video_path, easy=True)
        return metadata
    except Exception as e:
        print(f"Error extracting existing metadata: {str(e)}")
        return None

def set_metadata(video_path, metadata):
    try:
        metadata.save(video_path)
        print("Metadata saved successfully.")
    except Exception as e:
        print(f"Error saving metadata: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Edit metadata of a video file.")
    parser.add_argument("video_file", nargs="?", help="Video file to edit")
    args = parser.parse_args()

    if args.video_file:
        video_path = args.video_file
    else:
        # Check if a file was dropped onto the script
        for line in fileinput.input():
            video_path = line.strip()
            break

    if not video_path:
        print("Usage: python video_metadata_editor.py <video_file>")
        sys.exit(1)

    if not os.path.isfile(video_path):
        print(f"File not found: {video_path}")
        sys.exit(1)

    # Extract and display existing metadata
    print("Existing Metadata:")
    existing_metadata = get_existing_metadata(video_path)
    if existing_metadata:
        print(existing_metadata)

    # Extract and display video metadata
    print("\nVideo Metadata:")
    duration, resolution, codec = extract_metadata(video_path)
    print(f"Duration: {duration} seconds")
    print(f"Resolution: {resolution}")
    print(f"Codec: {codec} fps")

    # Allow the user to modify metadata
    metadata_title = input("Enter a new title (Press Enter to keep existing title): ")
    if metadata_title:
        existing_metadata["title"] = metadata_title

    # Save modified metadata
    set_metadata(video_path, existing_metadata)

if __name__ == "__main__":
    main()
