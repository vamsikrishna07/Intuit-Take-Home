from ActivityManager import ActivityManager

def main():
    file_path_prefix, file_path_suffix = 'secret-message.', '.txt'
    for index in range(6):
        file_path = file_path_prefix + str(index) + file_path_suffix
        activity = ActivityManager(file_path=file_path, index=index)
        activity.start()
if __name__ == '__main__':
    main()