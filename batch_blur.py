import os
import random
from pathlib import Path
from motionblur import Kernel  # 假设你的 motionblur.py 在同一目录下

def batch_process_images(input_folder, output_folder):
    """
    读取 input_folder 中的所有图片，
    为每张图片生成随机的运动模糊核，
    并将结果保存到 output_folder。
    """
    # 确保输出目录存在
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    # 支持的图片扩展名
    valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}

    # 遍历文件夹
    for file_path in input_path.iterdir():
        if file_path.suffix.lower() in valid_extensions:
            try:
                print(f"正在处理: {file_path.name}...")

                # --- 核心修改部分 ---
                # 1. 随机生成模糊核的大小 (例如 30 到 100 像素之间)
                # 注意：Kernel 要求 size 是 tuple(int, int)
                random_size = random.randint(20, 35)
                
                # 2. 随机生成模糊强度 (0 到 1 之间)
                # 强度决定了轨迹的非线性程度
                random_intensity = random.uniform(0.1, 0.3)

                # 3. 为当前图片实例化一个新的 Kernel
                # 每次实例化都会调用 _createPath 生成全新的随机路径
                k = Kernel(size=(random_size, random_size), intensity=random_intensity)

                # 4. 应用模糊
                # applyTo 支持文件路径，返回一个 PIL Image 对象
                blurred_image = k.applyTo(file_path, keep_image_dim=True)

                # 5. 保存结果
                output_file = output_path / f"blurred_{file_path.name}"
                blurred_image.save(output_file)
                print(f"已保存: {output_file}")

            except Exception as e:
                print(f"处理图片 {file_path.name} 时出错: {e}")

if __name__ == '__main__':
    #在此处修改你的输入和输出文件夹路径
    INPUT_DIR = "gt" 
    OUTPUT_DIR = "blur"
    
    batch_process_images(INPUT_DIR, OUTPUT_DIR)