#!/usr/bin/env python3
"""创建牛奶图片：玻璃杯装牛奶"""

from PIL import Image, ImageDraw
import os

def create_milk_image(output_path, size=400):
    """创建一个玻璃杯装牛奶的图片"""
    # 创建透明背景的图片
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = size // 2, size // 2
    
    # 玻璃杯尺寸
    glass_width = 120
    glass_height = 180
    glass_x = center_x - glass_width // 2
    glass_y = center_y - glass_height // 2 + 20
    
    # 颜色定义
    glass_color = (240, 248, 255, 100)      # 浅蓝色半透明（玻璃）
    glass_outline = (176, 196, 222, 255)     # 浅钢蓝色边框
    milk_color = (255, 255, 255, 240)        # 白色牛奶
    milk_top = (250, 250, 255, 255)          # 牛奶表面
    
    # 绘制玻璃杯（梯形）
    # 杯子底部
    bottom_width = glass_width - 20
    bottom_x = center_x - bottom_width // 2
    bottom_y = glass_y + glass_height
    
    # 杯身（用多边形绘制梯形）
    glass_points = [
        (glass_x, glass_y),                    # 左上
        (glass_x + glass_width, glass_y),      # 右上
        (bottom_x + bottom_width, bottom_y),   # 右下
        (bottom_x, bottom_y)                   # 左下
    ]
    
    # 杯子内部（牛奶）
    milk_margin = 8
    milk_top_y = glass_y + 25  # 牛奶液面位置
    
    milk_points = [
        (glass_x + milk_margin, milk_top_y),
        (glass_x + glass_width - milk_margin, milk_top_y),
        (bottom_x + bottom_width - milk_margin, bottom_y - 5),
        (bottom_x + milk_margin, bottom_y - 5)
    ]
    
    # 绘制牛奶（在杯子里面）
    draw.polygon(milk_points, fill=milk_color)
    
    # 牛奶表面（椭圆）
    milk_surface_y = milk_top_y
    draw.ellipse([glass_x + milk_margin, milk_surface_y - 15,
                 glass_x + glass_width - milk_margin, milk_surface_y + 15],
                fill=milk_top, outline=(245, 245, 250, 255), width=1)
    
    # 牛奶表面的高光
    highlight_x = center_x - 15
    highlight_y = milk_surface_y - 5
    draw.ellipse([highlight_x - 20, highlight_y - 3,
                 highlight_x + 20, highlight_y + 3],
                fill=(255, 255, 255, 255))
    
    # 绘制玻璃杯轮廓
    draw.polygon(glass_points, outline=glass_outline, width=3)
    
    # 杯口（椭圆）
    draw.ellipse([glass_x - 5, glass_y - 15,
                 glass_x + glass_width + 5, glass_y + 15],
                outline=glass_outline, width=3)
    
    # 玻璃杯上的高光（左侧）
    highlight_points = [
        (glass_x + 15, glass_y + 30),
        (glass_x + 25, glass_y + 30),
        (glass_x + 20, bottom_y - 30),
        (glass_x + 10, bottom_y - 30)
    ]
    draw.polygon(highlight_points, fill=(255, 255, 255, 80))
    
    # 杯底阴影
    draw.ellipse([bottom_x - 5, bottom_y - 8,
                 bottom_x + bottom_width + 5, bottom_y + 8],
                fill=(200, 200, 200, 60))
    
    # 保存图片
    img.save(output_path, 'PNG')
    print(f"✓ 创建牛奶图片: {output_path}")
    return output_path

if __name__ == "__main__":
    # 创建images目录
    img_dir = "images"
    os.makedirs(img_dir, exist_ok=True)
    
    # 创建牛奶图片
    output_path = os.path.join(img_dir, "milk.png")
    create_milk_image(output_path, size=400)
    print("牛奶图片创建完成！")
