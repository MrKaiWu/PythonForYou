import os
cwd = os.getcwd()

def list_file(path=cwd,filetype = 'py'):
    '''
功能：
返回目标路径下特定文件类型的所有文件的绝对路径

返回类型：
list

函数参数：
path:目标路径
filetype：文件类型（用拓展名表示）
    '''

    filelist=[]
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1].lower()==filetype:            
                absolutepath=os.path.join(dirpath,filename)
                filelist.append(absolutepath)
    return filelist

