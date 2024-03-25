import sys
import os

if __name__ == '__main__':
    path = sys.argv[1]
    dir_name = sys.argv[1].split('/')[-1]
    os.makedirs(dir_name, exist_ok=True)
    os.system(f'cp -r {path}/doc {dir_name}')
    os.system(f'cp -r {path}/in {dir_name}')
    os.system(f'cp -r {path}/out {dir_name}')
    os.system(f'cp -r {path}/prog {dir_name}')
    os.system(f'cp -r {path}/config.yml {dir_name}')
    path = 'pkg' + path[3:]
    os.system(f'7z a -tzip {path}.zip {dir_name}')
    os.system(f'rm -rf {dir_name}')
