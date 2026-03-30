#!/usr/bin/env python3
"""
英语单词卡片生成系统
- 管理单词列表
- 生成图片
- 创建Word文档
- 提供例句和短语
"""

import json
import os
from datetime import datetime

# 单词数据库文件路径
WORD_DB_PATH = "word_database.json"

# 初始化单词数据库
def init_word_database():
    """初始化或加载单词数据库"""
    if os.path.exists(WORD_DB_PATH):
        with open(WORD_DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # 创建初始单词列表
        initial_data = {
            "metadata": {
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_words": 13
            },
            "words": {
                "Dog": {
                    "chinese": "小狗",
                    "category": "animals",
                    "emoji": "🐕",
                    "color": "#FF8C00",
                    "bg": "FFF8DC",
                    "difficulty": 1,
                    "phrases": [
                        "This is a dog.",
                        "I have a dog.",
                        "The dog is cute."
                    ],
                    "sentences": [
                        "Look at the dog! It's running.",
                        "My dog likes to play with a ball.",
                        "Can you say 'dog'?"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Cat": {
                    "chinese": "小猫",
                    "category": "animals",
                    "emoji": "🐱",
                    "color": "#FFB6C1",
                    "bg": "FFF0F5",
                    "difficulty": 1,
                    "phrases": [
                        "This is a cat.",
                        "I see a cat.",
                        "The cat is sleeping."
                    ],
                    "sentences": [
                        "The cat says 'meow'.",
                        "Do you like cats?",
                        "The cat is drinking milk."
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Mouse": {
                    "chinese": "老鼠",
                    "category": "animals",
                    "emoji": "🐭",
                    "color": "#A9A9A9",
                    "bg": "F5F5F5",
                    "difficulty": 1,
                    "phrases": [
                        "A little mouse.",
                        "The mouse is small.",
                        "I see a mouse."
                    ],
                    "sentences": [
                        "The mouse likes cheese.",
                        "Be quiet like a mouse!",
                        "The mouse runs fast."
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Lion": {
                    "chinese": "狮子",
                    "category": "animals",
                    "emoji": "🦁",
                    "color": "#FFD700",
                    "bg": "FFFACD",
                    "difficulty": 2,
                    "phrases": [
                        "A big lion.",
                        "The lion is strong.",
                        "I hear a lion."
                    ],
                    "sentences": [
                        "The lion is the king of the jungle.",
                        "Lions say 'roar'!",
                        "Look at the lion's mane."
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Leopard": {
                    "chinese": "豹子",
                    "category": "animals",
                    "emoji": "🐆",
                    "color": "#CD853F",
                    "bg": "FAEBD7",
                    "difficulty": 2,
                    "phrases": [
                        "A spotted leopard.",
                        "The leopard runs fast.",
                        "Look at the leopard."
                    ],
                    "sentences": [
                        "Leopards have spots.",
                        "The leopard is climbing a tree.",
                        "Can you spot the leopard?"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Apple": {
                    "chinese": "苹果",
                    "category": "food",
                    "emoji": "🍎",
                    "color": "#DC143C",
                    "bg": "FFE4E1",
                    "difficulty": 1,
                    "phrases": [
                        "A red apple.",
                        "I eat an apple.",
                        "Yummy apple!"
                    ],
                    "sentences": [
                        "An apple a day keeps the doctor away!",
                        "Do you want an apple?",
                        "I like to eat apples."
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Cheese": {
                    "chinese": "奶酪",
                    "category": "food",
                    "emoji": "🧀",
                    "color": "#FFD700",
                    "bg": "FFFACD",
                    "difficulty": 1,
                    "phrases": [
                        "Yellow cheese.",
                        "I like cheese.",
                        "Tasty cheese!"
                    ],
                    "sentences": [
                        "Mice love cheese!",
                        "The cheese is yellow.",
                        "Do you want some cheese?"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Bread": {
                    "chinese": "面包",
                    "category": "food",
                    "emoji": "🍞",
                    "color": "#DEB887",
                    "bg": "FAEBD7",
                    "difficulty": 1,
                    "phrases": [
                        "Fresh bread.",
                        "I eat bread.",
                        "Soft bread."
                    ],
                    "sentences": [
                        "I like bread for breakfast.",
                        "The bread smells good.",
                        "Would you like some bread?"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Lollipop": {
                    "chinese": "棒棒糖",
                    "category": "food",
                    "emoji": "🍭",
                    "color": "#FF69B4",
                    "bg": "FFE4E6",
                    "difficulty": 1,
                    "phrases": [
                        "A sweet lollipop.",
                        "I love lollipops!",
                        "Colorful lollipop."
                    ],
                    "sentences": [
                        "Can I have a lollipop?",
                        "The lollipop is pink and sweet.",
                        "Don't eat too many lollipops!"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Milk": {
                    "chinese": "牛奶",
                    "category": "food",
                    "emoji": "🥛",
                    "color": "#87CEEB",
                    "bg": "E6F3FF",
                    "difficulty": 1,
                    "use_image": True,
                    "phrases": [
                        "A glass of milk.",
                        "Drink your milk.",
                        "White milk."
                    ],
                    "sentences": [
                        "Milk is good for you.",
                        "I drink milk every morning.",
                        "The cat wants some milk."
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Yogurt": {
                    "chinese": "酸奶",
                    "category": "food",
                    "emoji": "🥄",
                    "color": "#E91E63",
                    "bg": "FCE4EC",
                    "difficulty": 1,
                    "use_image": True,
                    "phrases": [
                        "A bowl of yogurt.",
                        "Eat yogurt with a spoon.",
                        "Pink yogurt."
                    ],
                    "sentences": [
                        "Yogurt is healthy and yummy.",
                        "I like strawberry yogurt.",
                        "Use a spoon to eat yogurt."
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Elephant": {
                    "chinese": "大象",
                    "category": "animals",
                    "emoji": "🐘",
                    "color": "#708090",
                    "bg": "F5F5F5",
                    "difficulty": 2,
                    "phrases": [
                        "A big elephant.",
                        "The elephant has a trunk.",
                        "Gray elephant."
                    ],
                    "sentences": [
                        "Elephants are the biggest land animals.",
                        "The elephant is using its trunk.",
                        "Look at the elephant's big ears!"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                },
                "Donut": {
                    "chinese": "甜甜圈",
                    "category": "food",
                    "emoji": "🍩",
                    "color": "#FF69B4",
                    "bg": "FFE4E6",
                    "difficulty": 1,
                    "phrases": [
                        "A round donut.",
                        "Sweet donut!",
                        "I love donuts."
                    ],
                    "sentences": [
                        "Donuts have a hole in the middle.",
                        "The donut has pink frosting.",
                        "This donut is delicious!"
                    ],
                    "added_at": datetime.now().strftime("%Y-%m-%d")
                }
            }
        }
        
        with open(WORD_DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)
        
        return initial_data

def add_word(word, chinese, category, emoji, color, bg, difficulty=1, phrases=None, sentences=None):
    """添加新单词到数据库"""
    db = init_word_database()
    
    if word in db["words"]:
        print(f"⚠️  单词 '{word}' 已存在！")
        return False
    
    db["words"][word] = {
        "chinese": chinese,
        "category": category,
        "emoji": emoji,
        "color": color,
        "bg": bg,
        "difficulty": difficulty,
        "phrases": phrases or [f"This is a {word.lower()}."],
        "sentences": sentences or [f"Look at the {word.lower()}!"],
        "added_at": datetime.now().strftime("%Y-%m-%d")
    }
    
    db["metadata"]["total_words"] = len(db["words"])
    db["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(WORD_DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已添加单词: {word} ({chinese})")
    return True

def get_all_words():
    """获取所有单词"""
    db = init_word_database()
    return list(db["words"].keys())

def get_word_info(word):
    """获取单词详细信息"""
    db = init_word_database()
    return db["words"].get(word)

def get_words_by_category(category):
    """按类别获取单词"""
    db = init_word_database()
    return {word: info for word, info in db["words"].items() 
            if info["category"] == category}

def get_phrases_for_word(word):
    """获取单词的短语和例句"""
    db = init_word_database()
    if word in db["words"]:
        return {
            "phrases": db["words"][word]["phrases"],
            "sentences": db["words"][word]["sentences"]
        }
    return None

def print_word_list():
    """打印所有单词列表"""
    db = init_word_database()
    print("\n" + "="*60)
    print("📚 当前单词列表")
    print("="*60)
    
    categories = {}
    for word, info in db["words"].items():
        cat = info["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(word)
    
    for category, words in categories.items():
        print(f"\n【{category.upper()}】")
        for word in words:
            info = db["words"][word]
            print(f"  • {word} ({info['chinese']}) - 难度: {'⭐' * info['difficulty']}")
    
    print(f"\n总计: {db['metadata']['total_words']} 个单词")
    print(f"最后更新: {db['metadata']['last_updated']}")
    print("="*60 + "\n")

if __name__ == "__main__":
    # 初始化数据库
    db = init_word_database()
    print("✅ 单词数据库已初始化")
    print_word_list()
