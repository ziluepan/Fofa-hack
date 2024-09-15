import sys

# 检查是否传入了文件名参数
if len(sys.argv) != 2:
    print("使用方法: python3 main.py <filename>")
    sys.exit(1)

# 获取输入文件名（同时也是输出文件名）
filename = sys.argv[1]

# 读取文件并去重
with open(filename, 'r') as file:
    lines = file.readlines()

# 使用集合去除重复项，同时保持原始顺序
unique_lines = list(dict.fromkeys(lines))

# 将去重后的内容写回文件
with open(filename, 'w') as file:
    file.writelines(unique_lines)

print(f"去重操作完成，已将结果写回 {filename}。")




