#!/usr/bin/env python3
"""生成儿童英语单词卡片图片"""

from PIL import Image, ImageDraw, ImageFont
import os

# 单词列表
words = [
    "Dog", "Cat", "Mouse", "Lion", "Leopard",
    "Apple", "Cheese", "Bread", "Lollipop", "Milk",
    "Yogurt", "Elephant", "Donut"
]

# 为每个单词创建简单的彩色图标
def create_icon(word, output_path):
    """创建一个简单的彩色图标"""
    # 创建白色背景的图片
    size = 400
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    # 根据单词选择颜色和形状
    colors = {
        'Dog': '#FFA500',      # 橙色
        'Cat': '#FFD700',      # 金色
        'Mouse': '#808080',    # 灰色
        'Lion': '#FFD700',     # 金色
        'Leopard': '#D2691E',  # 巧克力色
        'Apple': '#FF0000',    # 红色
        'Cheese': '#FFD700',   # 金色
        'Bread': '#DEB887',    # 棕色
        'Lollipop': '#FF69B4', # 粉色
        'Milk': '#FFFFFF',     # 白色
        'Yogurt': '#FFF8DC',   # 米色
        'Elephant': '#808080', # 灰色
        'Donut': '#DEB887'     # 棕色
    }
    
    color = colors.get(word, '#3498db')
    
    # 根据单词类型绘制不同的形状
    if word in ['Dog', 'Cat', 'Mouse', 'Lion', 'Leopard', 'Elephant']:
        # 动物 - 绘制圆角矩形作为身体
        margin = 60
        draw.rounded_rectangle([margin, margin, size-margin, size-margin], 
                              radius=50, fill=color, outline='#333333', width=3)
        # 添加简单的眼睛
        eye_size = 20
        draw.ellipse([140, 150, 140+eye_size, 150+eye_size], fill='black')
        draw.ellipse([240, 150, 240+eye_size, 150+eye_size], fill='black')
        # 添加嘴巴
        draw.arc([150, 220, 250, 280], start=0, end=180, fill='black', width=3)
        
    elif word in ['Apple']:
        # 苹果 - 圆形
        margin = 80
        draw.ellipse([margin, margin, size-margin, size-margin], 
                    fill=color, outline='#228B22', width=3)
        # 茎
        draw.rectangle([195, 60, 205, 90], fill='#8B4513')
        # 叶子
        draw.ellipse([205, 70, 240, 100], fill='#228B22')
        
    elif word in ['Cheese']:
        # 奶酪 - 三角形
        points = [(200, 60), (80, 320), (320, 320)]
        draw.polygon(points, fill=color, outline='#FFA500')
        # 添加孔洞
        draw.ellipse([150, 200, 180, 230], fill='#FFD700')
        draw.ellipse([220, 250, 260, 290], fill='#FFD700')
        
    elif word in ['Bread']:
        # 面包 - 椭圆
        draw.ellipse([60, 100, 340, 300], fill=color, outline='#CD853F', width=3)
        # 添加纹理线条
        draw.arc([100, 150, 300, 250], start=200, end=340, fill='#CD853F', width=2)
        
    elif word in ['Lollipop']:
        # 棒棒糖 - 圆形+棍子
        draw.ellipse([100, 60, 300, 260], fill=color, outline='#FF1493', width=3)
        # 螺旋条纹
        for i in range(0, 360, 40):
            draw.arc([120, 80, 280, 240], start=i, end=i+20, fill='white', width=5)
        # 棍子
        draw.rectangle([190, 260, 210, 340], fill='white', outline='#DDD', width=2)
        
    elif word in ['Milk', 'Yogurt']:
        # 牛奶/酸奶 - 杯子形状
        # 杯身
        draw.rectangle([100, 100, 300, 300], fill=color, outline='#333', width=3)
        # 杯顶
        draw.ellipse([90, 80, 310, 130], fill=color, outline='#333', width=3)
        # 杯底
        draw.ellipse([90, 270, 310, 320], fill=color, outline='#333', width=3)
        # 标签
        draw.rectangle([120, 150, 280, 220], fill='#4169E1', outline='#333', width=2)
        
    elif word in ['Donut']:
        # 甜甜圈 - 圆环
        draw.ellipse([60, 60, 340, 340], fill=color, outline='#CD853F', width=3)
        draw.ellipse([140, 140, 260, 260], fill='white')  # 中心孔
        # 糖霜
        draw.ellipse([70, 70, 330, 330], outline='#FF69B4', width=15)
        # 彩色糖粒
        import random
        random.seed(word)
        for _ in range(15):
            x = random.randint(100, 300)
            y = random.randint(100, 300)
            size = random.randint(5, 10)
            c = random.choice(['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF'])
            draw.ellipse([x, y, x+size, y+size], fill=c)
    
    # 在底部添加单词标签（大号字体）
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
    except:
        font = ImageFont.load_default()
    
    # 计算文本位置（居中）
    bbox = draw.textbbox((0, 0), word, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (size - text_width) // 2
    text_y = size - 70
    
    # 绘制文字阴影
    draw.text((text_x+2, text_y+2), word, fill='#666', font=font)
    # 绘制文字
    draw.text((text_x, text_y), word, fill='#333', font=font)
    
    # 保存图片
    img.save(output_path)
    print(f"Created: {output_path}")

# 主程序
if __name__ == "__main__":
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)
    
    for word in words:
        output_path = os.path.join(output_dir, f"{word.lower()}.png")
        create_icon(word, output_path)
    
    print(f"\n总共生成了 {len(words)} 张图片")
