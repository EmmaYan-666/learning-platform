#!/usr/bin/env python3
"""
添加新单词示例
演示如何向单词数据库中添加新单词
"""

from word_list_manager import add_word, print_word_list

def add_new_words():
    """添加新单词到数据库"""
    
    print("\n" + "="*60)
    print("📝 添加新单词示例")
    print("="*60 + "\n")
    
    # 示例：添加一些新单词
    
    # 1. 添加动物类单词
    add_word(
        word="Bird",
        chinese="小鸟",
        category="animals",
        emoji="🐦",
        color="#3498DB",
        bg="EBF5FB",
        difficulty=1,
        phrases=[
            "A little bird.",
            "The bird can fly.",
            "I see a bird."
        ],
        sentences=[
            "Look at the bird in the tree!",
            "The bird is singing.",
            "Birds have wings and can fly."
        ]
    )
    
    add_word(
        word="Fish",
        chinese="鱼",
        category="animals",
        emoji="🐟",
        color="#5DADE2",
        bg="E8F6F3",
        difficulty=1,
        phrases=[
            "A small fish.",
            "The fish swims.",
            "I like fish."
        ],
        sentences=[
            "Fish live in water.",
            "The fish is swimming in the pond.",
            "Can you see the colorful fish?"
        ]
    )
    
    # 2. 添加食物类单词
    add_word(
        word="Banana",
        chinese="香蕉",
        category="food",
        emoji="🍌",
        color="#F4D03F",
        bg="FEF9E7",
        difficulty=1,
        phrases=[
            "A yellow banana.",
            "I eat a banana.",
            "Sweet banana!"
        ],
        sentences=[
            "Monkeys love bananas!",
            "The banana is yellow and sweet.",
            "Would you like a banana?"
        ]
    )
    
    add_word(
        word="Cake",
        chinese="蛋糕",
        category="food",
        emoji="🎂",
        color="#E91E63",
        bg="FCE4EC",
        difficulty=1,
        phrases=[
            "A birthday cake.",
            "Yummy cake!",
            "I love cake."
        ],
        sentences=[
            "Happy birthday! Here's a cake for you.",
            "The cake has candles on it.",
            "Let's eat cake together!"
        ]
    )
    
    # 3. 添加家庭类单词（新类别）
    add_word(
        word="Mom",
        chinese="妈妈",
        category="family",
        emoji="👩",
        color="#E91E63",
        bg="FCE4EC",
        difficulty=1,
        phrases=[
            "My mom.",
            "I love mom.",
            "Mom is here."
        ],
        sentences=[
            "Mom is cooking dinner.",
            "I love my mom very much.",
            "Mom reads me a story."
        ]
    )
    
    add_word(
        word="Dad",
        chinese="爸爸",
        category="family",
        emoji="👨",
        color="#2196F3",
        bg="E3F2FD",
        difficulty=1,
        phrases=[
            "My dad.",
            "Dad is tall.",
            "I love dad."
        ],
        sentences=[
            "Dad is playing with me.",
            "My dad is strong.",
            "Dad helps me with homework."
        ]
    )
    
    print("\n✅ 新单词添加完成！\n")
    
    # 打印更新后的单词列表
    print_word_list()

if __name__ == "__main__":
    add_new_words()
