from subprocess import call
import os

# Define input and output directories
input_dir = '/Users/arhamkhurram/Documents/Image Dump/Webm Files'
output_dir_stickers = '/Users/arhamkhurram/Documents/Image Dump/Stickers'  # Change this to your desired webp output directory
output_dir_gifs = '/Users/arhamkhurram/Documents/Image Dump/Gifs'  # Change this to your desired webm output directory

# List to store filename present in the current directory
files = []
webp = []
webm = []

# Iterate over files in the input directory
for file_path in os.listdir(input_dir):
    if os.path.isfile(os.path.join(input_dir, file_path)):
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension == '.webp':
            webp.append(file_path)
        elif file_extension == '.webm':
            webm.append(file_path)

print("WebP Files:")
for file in webp:
    print(file)
    # Define the output file path (inside the loop)
    file_name, _ = os.path.splitext(file)
    output_file = os.path.join(output_dir_stickers, f"{file_name}.jpeg")
    # Run FFmpeg to convert WebP to JPEG
    return_code = call(["ffmpeg", "-i", os.path.join(input_dir, file), output_file])
    if return_code == 0:
        # Conversion successful, remove the original WebP file
        os.remove(os.path.join(input_dir, file))
    else:
        print(f"Conversion of {file} failed!")

print("\nWebM Files:")
for file in webm:
    print(file)
    # Define the output file path (inside the loop)
    file_name, _ = os.path.splitext(file)
    output_file = os.path.join(output_dir_gifs, f"{file_name}.gif")
    # Run FFmpeg to convert WebM to GIF
    return_code = call(["ffmpeg", "-i", os.path.join(input_dir, file), output_file])
    if return_code == 0:
        # Conversion successful, remove the original WebM file
        os.remove(os.path.join(input_dir, file))
    else:
        print(f"Conversion of {file} failed!")
