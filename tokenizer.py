#%%
import spacy 
import sys
import os 

#%%
print('Initializing...')
nlp = spacy.load('en_core_web_sm')

#%%
def read_dir(input_dir, output_dir):
    files = os.listdir(input_dir)
    for file in files:
        try:
            tokenize_to_file(input_dir, file, output_dir)
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print(file)

def tokenize_to_file(input_dir, filename, output_dir):
    if not os.path.isfile(os.path.join(output_dir, filename)):
        file_text = open(os.path.join(input_dir, filename)).read()
        tokenized_file_doc = nlp(file_text)

        f = open(os.path.join(output_dir, filename), 'w')

        # import pdb; pdb.set_trace()
        for token in tokenized_file_doc:
            f.writelines(f'{token.text} O\n')
        f.close()

def main(input_dir: str, output_dir: str):
    read_dir(input_dir, output_dir)

if __name__ == '__main__':
    main(*sys.argv[1:])