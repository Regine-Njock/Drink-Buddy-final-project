from PIL import Image
import os

def resize_images(input_folder, output_folder, size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            # Open the image file
            with Image.open(input_path) as img:
                # Resize the image while maintaining the aspect ratio
                img.thumbnail(size)
                # Save the resized image
                img.save(output_path)
                print(f"Resized {file_name} successfully.")
        except Exception as e:
            print(f"Failed to resize {file_name}: {str(e)}")

# Set the input folder, output folder, and desired size
input_folder = "/home/dci-student/Final_Project/Drink_Buddy/Drink_Buddy/media/images/recipes/"
output_folder = "/home/dci-student/Final_Project/Drink_Buddy/Drink_Buddy/media/images/recipes2/"
size = (400, 600)  # Set the desired width and height

# Call the resize_images function
resize_images(input_folder, output_folder, size)
