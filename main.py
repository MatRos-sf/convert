from PIL import Image
from os import listdir, remove

PATH = 'foto/'
FILES = sorted(listdir(PATH))

def convert_jpg_to_pdf():
    # check if we have file jpg
    if not FILES:
        raise FileNotFoundError("We don't have find jpg file. Directory foto can't be empty!")

    image_list = []
    for name_jpg in FILES:
        if name_jpg[-4:] in ('.jpg', '.JPG') or name_jpg[-5:] in ('.jpeg', '.JPEG'):
            img = Image.open(PATH+name_jpg)
            image_list.append(img.convert('RGB'))

    name_pdf = input("How do you call the new pdf file? [don't add suffix]: ")

    if name_pdf[-4:] != '.pdf' or name_pdf[-4:] != '.PDF':
        name_pdf += '.pdf'

    # save
    first_image = image_list.pop(0)
    first_image.save('pdf_files/'+name_pdf, save_all=True, append_images=image_list)

    #remove jpg file
    for file in FILES:
        if name_jpg[-4:] in ('.jpg', '.JPG') or name_jpg[-5:] in ('.jpeg', '.JPEG'):
            remove(PATH+file)


if __name__ == '__main__':
    convert_jpg_to_pdf()

