import os
import ffmpeg


class Convertor:
    def __init__(self, path = './'):
        self.path = 'D:\Downloads/'

    def get_files(self):
        return os.listdir(self.path)

    def search_file_type(self, file_type):
        files = self.get_files()
        valid_arr = []
        files_name = []

        for file in files:
            split_tup = os.path.splitext(file)

            if split_tup[1] == file_type:
                valid_arr.append(file)
                files_name.append(split_tup[0])

        return valid_arr, files_name

    def start_convert(self, input, output):
            stream = ffmpeg.input(input)
            stream = ffmpeg.hflip(stream)
            stream = ffmpeg.output(stream, output)
            ffmpeg.run(stream)

    def create_output_dir(self):
        os.mkdir(self.path + 'output')

    def webm_to_gif(self):
        valid_files, files_name = self.search_file_type('.webm')

        self.create_output_dir()

        for i in range(len(valid_files)):
            self.start_convert(self.path + valid_files[i], f'{self.path}output/{files_name[i]}.gif')

        return 'Done'

    def mp4_to_gif():
        pass

    def jpeg_to_png():
        pass

if __name__ == '__main__':
    c = Convertor()
    c.webm_to_gif()