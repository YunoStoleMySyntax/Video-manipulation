import argparse
import moviepy.editor as mp

def calculate_fps(video_path):
    clip = mp.VideoFileClip(video_path)
    return clip.fps

def lower_fps(video_path, output_path, target_fps):
    clip = mp.VideoFileClip(video_path)
    modified_clip = clip.set_fps(target_fps)
    modified_clip.write_videofile(output_path, codec="libx264")

def main():
    parser = argparse.ArgumentParser(description="Lower the FPS of a video file.")
    parser.add_argument("input_file", help="Path to the input video file.")
    parser.add_argument("-t", "--target_fps", type=float, default=None, help="Target FPS for the output video.")
    args = parser.parse_args()

    input_file = args.input_file

    current_fps = calculate_fps(input_file)
    print(f"Current FPS: {current_fps:.2f}")

    if args.target_fps is None:
        target_fps = float(input("Enter the target FPS: "))
    else:
        target_fps = args.target_fps

    output_file = input_file.replace(".mp4", f"-lowerFPS.mp4")
    lower_fps(input_file, output_file, target_fps)

    print(f"Video saved with lower FPS at {target_fps} FPS: {output_file}")

if __name__ == "__main__":
    main()
