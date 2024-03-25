import sys
import os

def clean():
    os.system(f'rm -rf {dir_name}')


if __name__ == '__main__':
    path = sys.argv[1]
    dir_name = sys.argv[1].split('/')[-1]

    print(f'Checking {path}...')
    assert os.path.exists(path), f'Path {path} does not exist'
    
    print(f'Checking {path}/doc...')
    assert os.path.exists(f'{path}/doc'), f'Path {path}/doc does not exist'
    doc_content = os.listdir(f'{path}/doc')
    doc_content = [file for file in doc_content if file.endswith('.pdf')]
    assert len(doc_content) == 1, f'Exactly one pdf file is required in {path}/doc'

    print(f'Checking {path}/in...')
    assert os.path.exists(f'{path}/in'), f'Path {path}/in does not exist'
    in_content = os.listdir(f'{path}/in')
    in_content = [file for file in in_content if file.endswith('.in')]
    assert len(in_content) > 20, f'At least 20 input files are required in {path}/in'

    print(f'Checking {path}/out...')
    assert os.path.exists(f'{path}/out'), f'Path {path}/out does not exist'
    out_content = os.listdir(f'{path}/out')
    assert len(out_content) < 4, f'At most 3 output files are allowed in {path}/out'

    print(f'Checking {path}/prog...')
    assert os.path.exists(f'{path}/prog'), f'Path {path}/prog does not exist'
    prog_content = os.listdir(f'{path}/prog')
    prog_content = [file for file in prog_content if file.endswith('.cpp') or file.endswith('.py')]
    assert len(prog_content) > 0, f'At least one source file is required in {path}/prog'

    print(f'Checking {path}/config.yml...')
    assert os.path.exists(f'{path}/config.yml'), f'Path {path}/config.yml does not exist'

    os.makedirs(dir_name, exist_ok=True)
    os.system(f'cp -r {path}/doc {dir_name}')
    os.system(f'cp -r {path}/in {dir_name}')
    os.system(f'cp -r {path}/out {dir_name}')
    os.system(f'cp -r {path}/prog {dir_name}')
    os.system(f'cp -r {path}/config.yml {dir_name}')
    path = 'pkg' + path[3:]
    os.system(f'7z a -tzip {path}.zip {dir_name}')
    clean()
