import os

def get_filename_list(path,pattern,filename):
        cmd = 'find ' + path + pattern + ' > ' + filename
        os.system(cmd)

def get_last_split_by_point(src_file_path,dst_file_path):
        with open(src_file_path, "r", encoding="utf-8") as fs:
                for i in fs.readlines():
                        with open(dst_file_path, "a", encoding="utf-8") as fd:
                                i = i.split('.')[-1]
                                fd.writelines(i)
        fs.close()
        fd.close()

def re_dup(src_file_path,dst_file_path):
        with open(src_file_path,"r+",encoding="utf-8") as f:
                content = f.readlines()
                content = set(content)
                with open(dst_file_path, "a+", encoding="utf-8") as f1:
                        for i in content:
                                print(i)
                                f1.writelines(i)
        f.close()
        f1.close()
