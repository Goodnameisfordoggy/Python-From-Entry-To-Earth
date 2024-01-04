#图片的复制,转化成jpg格式

def main():
    src_file_name = input("请输入文件名")
    try:
        with open(f'{src_file_name}', 'rb') as src_file:
            with open(f'copy_{src_file_name}', 'wb') as target_file:
                target_file.write(src_file.read())  # 边读边写
    except FileNotFoundError as e:
        print("指定的文件无法打开.")
    except IOError as e:
        print("读写文件时发生了错误!")


