import os


def read_files_from_folder(folder_path, extensions):
    files_content = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    non_empty_lines = [line for line in lines if line.strip()]
                    files_content.extend(non_empty_lines)

    return files_content


def write_lines_to_txt(lines, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    folder_path = "E:\project\src"  # 替换为你的文件夹路径
    output_file = "output.txt"
    extensions = ['.html', '.js','.vue']

    files_content = read_files_from_folder(folder_path, extensions)
    write_lines_to_txt(files_content, output_file)
