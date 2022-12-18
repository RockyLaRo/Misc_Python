from PIL import Image, GifImagePlugin
import datetime




def cut_image(im, piece_size):
  # Calculate the width and height of the image in pieces
  width, height = im.size
  num_pieces_x = width // piece_size
  num_pieces_y = height // piece_size

  # Loop through the pieces
  for i in range(num_pieces_x):
    # Create an empty list of images for the first frame in the column
    first_frame_images = []

    # Loop through the pieces in the row to process the first frame
    for j in range(1):
      # Calculate the coordinates of the piece
      x1 = i * piece_size
      y1 = j * piece_size
      x2 = x1 + piece_size
      y2 = y1 + piece_size

      # Crop the piece
      piece = im.crop((x1, y1, x2, y2))

      # Set the color #FF00FF to transparent
      piece = piece.convert("RGBA")
      data = piece.getdata()
      new_data = []
      for item in data:
        if item[0] == 255 and item[1] == 0 and item[2] == 255:
          new_data.append((255, 255, 255, 0))
        else:
          new_data.append(item)
      piece.putdata(new_data)

      # Add the piece to the list of images
      first_frame_images.append(piece)

    # Create an empty list of images for the remaining frames in the column
    remaining_frames_images = []

    # Loop through the pieces in the row to process the remaining frames
    for j in range(1, num_pieces_y):
      # Calculate the coordinates of the piece
      x1 = i * piece_size
      y1 = j * piece_size
      x2 = x1 + piece_size
      y2 = y1 + piece_size

      # Crop the piece
      piece = im.crop((x1, y1, x2, y2))

      # Set the color #FF00FF to transparent
      piece = piece.convert("RGBA")
      data = piece.getdata()
      new_data = []
      for item in data:
        if item[0] == 255 and item[1] == 0 and item[2] == 255:
          new_data.append((255, 255, 255, 0))
        else:
          new_data.append(item)
      piece.putdata(new_data)

      # Add the piece to the list of images
      remaining_frames_images.append(piece)

    # Set the timing for each frame to 10 milliseconds and the disposal method to "none"
    for image in first_frame_images:
      image.info['duration'] = 100
      image.info['disposal'] = 2

    for image in remaining_frames_images:
      image.info['duration'] = 100
      image.info['disposal'] = 2

    # Save the images as a GIF
    # Save the first frame of the row as a GIF

    file_name = f'row_{i}_first_frame_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.gif'
    first_frame_images[0].save(file_name, save_all=True, append_images=first_frame_images[1:], loop=0)


    # Save the remaining frames of the row as a GIF

    file_name = f'row_{i}_remaining_frames_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.gif'
    remaining_frames_images[0].save(file_name, save_all=True, append_images=remaining_frames_images[1:], loop=0)

# Open the image
im = Image.open('Creature_1534.png')

# Cut the image into pieces depending on the width
if im.width == 128:
  cut_image(im, 32)
elif im.width == 256:
  cut_image(im, 64)
elif im.height == 1024:
  cut_image(im, 128)
else:
  print("Error: Invalid image dimensions")
import os

# Get the list of all files in the folder
folder = ''
files = os.listdir(folder)

# Loop through the files
for file in files:
  # Open the image
  im = Image.open(os.path.join(folder, file))

  # Cut the image into pieces depending on the width
  if im.width == 128:
    cut_image(im, 32)
  elif im.width == 256:
    cut_image(im, 64)
  elif im.height == 1024:
    cut_image(im, 128)
  else:
    print("Error: Invalid image dimensions")
