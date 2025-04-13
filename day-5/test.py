import os

def check_string_in_file(filename, search_string):
    with open(filename, 'r', encoding='utf-8') as file:
        return search_string in file.read()

def check_string_in_folder(folder_path, search_string):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            if check_string_in_file(os.path.join(folder_path, filename), search_string):
                print(f"Found in {filename}")

def replace_name_in_file(template_file, names):
    with open(template_file, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    for name in names:
        new_content = template_content.replace("[name]", name)
        new_filename = f"output_{name}.txt"
        with open(new_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(new_content)
        print(f"Created {new_filename}")

def rotate_2d_list_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = [line.strip().split() for line in file.readlines()]
    rotated_data = list(map(list, zip(*data[::-1])))  # Rotate 90 degrees clockwise
    
    with open(filename, 'w', encoding='utf-8') as file:
        for row in rotated_data:
            file.write(" ".join(row) + "\n")
    print(f"Rotated data in {filename}")

# Example usage:
# check_string_in_file("example.txt", "search_term")
# check_string_in_folder("./test_folder", "search_term")
# replace_name_in_file("template.txt", ["Alice", "Bob", "Charlie"])
# rotate_2d_list_in_file("matrix.txt")