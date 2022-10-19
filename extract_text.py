# %%
import sys
from PyPDF2 import PdfReader
import os 

# %%
class ExtractText():
    # def __init__(self, paths):
    #     self.in_dir = paths[0]
    #     self.out_dir = paths[1]

    def file_read(self, in_loc, out_loc):
        # import pdb; pdb.set_trace()
        try:
            reader = PdfReader(in_loc)
            number_of_pages = len(reader.pages)
            page = reader.pages[0]
            text = page.extract_text()
            with open(out_loc, 'w') as f:
                # print('write first page.')
                f.write(text)

            for i in range(1, number_of_pages):
                page = reader.pages[i]
                text = page.extract_text()
                with open(out_loc, 'a') as f:
                    f.write(text)
                    
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print(in_loc)
            # raise

    def dir_read(self, in_dir, out_dir):
        files = os.listdir(in_dir)
        for file in files:
            fn = os.path.basename(os.path.splitext(file)[0]) + '.txt'
            # if file already exists, skip
            if os.path.isfile(os.path.join(out_dir, fn)):
                # print(f'file {fn} exists.')
                continue
            else:
                # print('will read file.')
                self.file_read(os.path.join(in_dir, file), os.path.join(out_dir, fn))

def main(in_dir: str, out_dir: str):
    # output location
    # input (file/folder)
    # select whether it's file or folder

    extract = ExtractText()
    extract.dir_read(in_dir, out_dir)

if __name__ == '__main__':
    main(*sys.argv[1:])
