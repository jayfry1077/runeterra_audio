import ffmpeg
import os

path_to_images = r'D:\\RiotAPI\\LOR\\img\\DE_cards_only\\'
path_for_loop = r'D:\\RiotAPI\\LOR\\img\\DE_cards_only\\'
path_to_audios = './examples/wav/'
path_to_saves = './videos/'
my_list = 'mylist.txt'

# def save():
#     os.system("ffmpeg -framerate 1/5 -i {}01DE%03d.png video.webm".format(path_to_images))

def save(path_to_image, path_to_audio, path_to_save):
    os.system("ffmpeg -threads 2 -loop 1 -i {} -i {} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {}.mp4".format(path_to_image, path_to_audio, path_to_save))

def concat():
    os.system('ffmpeg -f concat -safe 0 -i {} -c copy Demacia.mp4'.format(path_to_saves + 'mylist.txt'))


concat()

# for file in os.listdir(path_to_images):
#     save(path_to_images + file, path_to_audios + file.split('.')[0] + '.wav', path_to_saves + file.split('.')[0])

# with open(path_to_saves + 'mylist.txt', 'w') as f:
#     for file in os.listdir(path_to_images):
#         f.write('file {}\n'.format(file.replace('png', 'mp4')))
    
#     f.close()