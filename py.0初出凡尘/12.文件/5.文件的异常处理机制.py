def main():
    file = None
    try:
        file = open('5.文件的异常处理.txt', 'r', encoding='utf-8')
        print(file.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        #确保任何情况下都能关闭打开的文件
        if file:
            file.close()


if __name__ == '__main__':
    main()