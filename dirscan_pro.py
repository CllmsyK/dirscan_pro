import os

# 输出绝对路径
def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)

def filetypes(dirpath):
    filename = 'filepath.txt'
    f = open(filename, 'w+', encoding='utf-8', newline=None)
    f.write('当前目录绝对路径:' + dir_path + '\n')
    f.write('------------------------------' + '\n' + '\n')
    dirlist = []
    listdir(dirpath, dirlist)
    for dir in dirlist:
        f.write(dir.replace("\\", "/").replace(dirpath.replace("\\", "/"), "")+"\n")
    f.close()

# 输出树形图
def treeStructure(startpath):
    filename = 'tree.txt'
    f = open(filename, 'w+', encoding='utf-8', newline=None)
    f.write('\n' + '当前目录的树形图' + '\n')
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 2 * level
        f.write('{}|'.format(indent[:]) + '\n')
        f.write('{}+{}/'.format(indent, os.path.basename(root)) + '\n')
        subindent = ' ' * 2 * (level + 1)

        for file in files:
            f.write('{}| +--- {}'.format(subindent[:-2], file) + '\n')
    f.close()

def dst_dir_file(file_path, file_ext, list=[]):
    for item in os.listdir(file_path):
        path = os.path.join(file_path, item)
        if os.path.isdir(path):
            dst_dir_file(path, file_ext, list)
        if path.endswith(file_ext):
            list.append(path)
    return list

def type_ls():
    file_type = input('请输入文件类型(jpg,txt,png,py,php...)' + '\n')
    filename = file_type + '.txt'
    try:
        f = open(filename, 'w+', encoding='utf-8', newline=None)
        lists = dst_dir_file(dir_path, '.' + file_type)
        for file in lists:
            f.write(file + '\n')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # 获取当前路径
    dir_path = os.path.dirname(os.path.abspath(__file__))
    run_type = input('是否需要指定文件类型(y/n):' + '\n')
    if run_type != 'y':
        filetypes(dir_path)
        treeStructure(dir_path)
    else:
        type_ls()