import os


def find_recent_video():
    files_path = "C:\\HC\\videoList\\"
    file_list = []
    for f_name in os.listdir(f"{files_path}"):
        written_time = os.path.getctime(f"{files_path}{f_name}")
        file_list.append((f_name, written_time))
    # 생성시간 역순으로 정렬
    sorted_file_list = sorted(file_list, key=lambda x: x[1], reverse=True)
    # 가장 앞에있는 파일을 넣어줌
    recent_file = sorted_file_list[0]  # 첫번째꺼.
    recent_file_name = recent_file[0]
    check_video_path = files_path + str(recent_file_name)

    return check_video_path


def remove_Forder():
    file_list = []
    capture_folder_path = "C:\\HC\\onlyCaptureList\\"
    afterCrop_folder_path = "C:\\HC\\afterCrop\\"
    imgList_folder_path = "C:\\HC\\imgList\\"

    for f_name in os.listdir(f"{afterCrop_folder_path}"):
        print(afterCrop_folder_path + f_name)


remove_Forder()