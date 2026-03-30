#!/usr/bin/env python3
"""创建酸奶图片：碗装酸奶配勺子"""

from PIL import Image, ImageDraw
import os

def create_yogurt_image(output_path, size=400):
    """创建一个碗装酸奶配勺子的图片"""
    # 创建透明背景的图片
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 颜色定义
    yogurt_color = (255, 240, 245, 255)  # 浅粉色酸奶
    bowl_outer = (255, 255, 255, 255)     # 白色碗
    bowl_inner = (240, 240, 240, 255)     # 浅灰色碗内部
    spoon_color = (192, 192, 192, 255)    # 银色勺子
    spoon_handle = (169, 169, 169, 255)   # 深银色勺柄
    
    center_x, center_y = size // 2, size // 2
    
    # 绘制碗（椭圆形，从上方看）
    # 碗的外圈
    bowl_width = size * 0.65
    bowl_height = size * 0.35
    bowl_x1 = center_x - bowl_width // 2
    bowl_y1 = center_y - bowl_height // 2 + 30
    bowl_x2 = center_x + bowl_width // 2
    bowl_y2 = center_y + bowl_height // 2 + 30
    
    # 碗的底部（侧面）
    draw.ellipse([bowl_x1, bowl_y1, bowl_x2, bowl_y2 + 60], 
                 fill=(230, 230, 230, 255), outline=(200, 200, 200, 255), width=3)
    
    # 碗的上沿（从上方看的椭圆）
    draw.ellipse([bowl_x1, bowl_y1, bowl_x2, bowl_y2], 
                 fill=bowl_outer, outline=(200, 200, 200, 255), width=3)
    
    # 酸奶（在碗里面）
    yogurt_margin = 15
    yogurt_x1 = bowl_x1 + yogurt_margin
    yogurt_y1 = bowl_y1 + yogurt_margin // 2
    yogurt_x2 = bowl_x2 - yogurt_margin
    yogurt_y2 = bowl_y2 - yogurt_margin // 2
    
    draw.ellipse([yogurt_x1, yogurt_y1, yogurt_x2, yogurt_y2], 
                 fill=yogurt_color, outline=(255, 228, 225, 255), width=2)
    
    # 酸奶表面装饰（小圆点代表果粒或纹理）
    for i in range(8):
        import random
        random.seed(i + 42)
        dot_x = random.randint(int(yogurt_x1 + 20), int(yogurt_x2 - 20))
        dot_y = random.randint(int(yogurt_y1 + 10), int(yogurt_y2 - 10))
        dot_size = random.randint(5, 10)
        colors = [(255, 182, 193, 180), (255, 192, 203, 180), (255, 160, 180, 180)]
        dot_color = random.choice(colors)
        draw.ellipse([dot_x - dot_size, dot_y - dot_size//2, 
                     dot_x + dot_size, dot_y + dot_size//2], 
                    fill=dot_color)
    
    # 绘制勺子
    # 勺子柄（倾斜放置）
    handle_length = 120
    handle_width = 12
    handle_start_x = center_x + 80
    handle_start_y = center_y - 40
    handle_end_x = handle_start_x + handle_length
    handle_end_y = handle_start_y - handle_length
    
    # 勺子柄（用多边形绘制）
    handle_points = [
        (handle_start_x - handle_width//2, handle_start_y),
        (handle_start_x + handle_width//2, handle_start_y),
        (handle_end_x + handle_width//2 + 5, handle_end_y),
        (handle_end_x - handle_width//2 - 5, handle_end_y)
    ]
    draw.polygon(handle_points, fill=spoon_handle, outline=(128, 128, 128, 255))
    
    # 勺子头（椭圆形）
    spoon_head_x = handle_start_x
    spoon_head_y = handle_start_y + 20
    spoon_head_width = 40
    spoon_head_height = 25
    
    draw.ellipse([spoon_head_x - spoon_head_width//2, spoon_head_y - spoon_head_height//2,
                 spoon_head_x + spoon_head_width//2, spoon_head_y + spoon_head_height//2],
                fill=spoon_color, outline=(128, 128, 128, 255), width=2)
    
    # 勺子头上的高光
    highlight_x = spoon_head_x - 8
    highlight_y = spoon_head_y - 5
    draw.ellipse([highlight_x - 6, highlight_y - 4, highlight_x + 6, highlight_y + 4],
                fill=(220, 220, 220, 255))
    
    # 勺子上沾的酸奶
    draw.ellipse([spoon_head_x - 12, spoon_head_y + 5,
                 spoon_head_x + 12, spoon_head_y + 15],
                fill=yogurt_color, outline=(255, 228, 225, 255), width=1)
    
    # 保存图片
    img.save(output_path, 'PNG')
    print(f"✓ 创建酸奶图片: {output_path}")
    return output_path

if __name__ == "__main__":
    # 创建images目录
    img_dir = "images"
    os.makedirs(img_dir, exist_ok=True)
    
    # 创建酸奶图片
    output_path = os.path.join(img_dir, "yogurt.png")
    create_yogurt_image(output_path, size=400)
    print("酸奶图片创建完成！")
