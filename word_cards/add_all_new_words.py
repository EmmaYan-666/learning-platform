#!/usr/bin/env python3
"""
批量添加新单词
"""

from word_list_manager import add_word, print_word_list

def add_all_new_words():
    """添加所有新单词"""
    
    print("\n" + "="*60)
    print("📝 批量添加新单词")
    print("="*60 + "\n")
    
    # 1. 食物类新增
    add_word(
        word="Watermelon",
        chinese="西瓜",
        category="food",
        emoji="🍉",
        color="#2ECC71",
        bg="E8F8F5",
        difficulty=1,
        phrases=[
            "A big watermelon.",
            "Sweet watermelon.",
            "I like watermelon."
        ],
        sentences=[
            "Watermelon is my favorite fruit!",
            "The watermelon is green outside and red inside.",
            "Let's eat watermelon on a hot day."
        ]
    )
    
    add_word(
        word="Water",
        chinese="水",
        category="food",
        emoji="💧",
        color="#5DADE2",
        bg="EBF5FB",
        difficulty=1,
        phrases=[
            "Drink water.",
            "A glass of water.",
            "Fresh water."
        ],
        sentences=[
            "Water is good for you.",
            "I drink water every day.",
            "The plants need water."
        ]
    )
    
    add_word(
        word="Rice",
        chinese="米饭",
        category="food",
        emoji="🍚",
        color="#F39C12",
        bg="FEF9E7",
        difficulty=1,
        phrases=[
            "Eat rice.",
            "White rice.",
            "A bowl of rice."
        ],
        sentences=[
            "Rice is a healthy food.",
            "I eat rice for lunch.",
            "This rice is yummy!"
        ]
    )
    
    # 2. 动物类新增
    add_word(
        word="Monkey",
        chinese="猴子",
        category="animals",
        emoji="🐒",
        color="#D68910",
        bg="FEF5E7",
        difficulty=1,
        phrases=[
            "A funny monkey.",
            "The monkey climbs.",
            "Cute monkey!"
        ],
        sentences=[
            "Monkeys like to climb trees.",
            "The monkey is eating a banana.",
            "Look at that silly monkey!"
        ]
    )
    
    # 3. 颜色类
    add_word(
        word="Red",
        chinese="红色",
        category="colors",
        emoji="🔴",
        color="#E74C3C",
        bg="FADBD8",
        difficulty=1,
        phrases=[
            "Red apple.",
            "The color red.",
            "I see red."
        ],
        sentences=[
            "Apples are red.",
            "I like the red dress.",
            "The red ball is big."
        ]
    )
    
    add_word(
        word="Green",
        chinese="绿色",
        category="colors",
        emoji="🟢",
        color="#27AE60",
        bg="D5F5E3",
        difficulty=1,
        phrases=[
            "Green grass.",
            "The color green.",
            "Green leaves."
        ],
        sentences=[
            "Grass is green.",
            "I see a green frog.",
            "The tree has green leaves."
        ]
    )
    
    add_word(
        word="Blue",
        chinese="蓝色",
        category="colors",
        emoji="🔵",
        color="#3498DB",
        bg="D6EAF8",
        difficulty=1,
        phrases=[
            "Blue sky.",
            "The color blue.",
            "Blue bird."
        ],
        sentences=[
            "The sky is blue.",
            "I have a blue car.",
            "Blue is a beautiful color."
        ]
    )
    
    add_word(
        word="White",
        chinese="白色",
        category="colors",
        emoji="⚪",
        color="#BDC3C7",
        bg="F8F9F9",
        difficulty=1,
        phrases=[
            "White snow.",
            "The color white.",
            "White clouds."
        ],
        sentences=[
            "Snow is white.",
            "I see white clouds in the sky.",
            "The cat is white and fluffy."
        ]
    )
    
    add_word(
        word="Black",
        chinese="黑色",
        category="colors",
        emoji="⚫",
        color="#2C3E50",
        bg="F4F6F7",
        difficulty=1,
        phrases=[
            "Black cat.",
            "The color black.",
            "Black bird."
        ],
        sentences=[
            "The cat has black fur.",
            "I see a black bird.",
            "Black and white are opposite colors."
        ]
    )
    
    add_word(
        word="Brown",
        chinese="棕色",
        category="colors",
        emoji="🟤",
        color="#8B4513",
        bg="FAF0E6",
        difficulty=1,
        phrases=[
            "Brown bear.",
            "The color brown.",
            "Brown bread."
        ],
        sentences=[
            "The bear has brown fur.",
            "Chocolate is brown.",
            "I like brown shoes."
        ]
    )
    
    add_word(
        word="Yellow",
        chinese="黄色",
        category="colors",
        emoji="🟡",
        color="#F4D03F",
        bg="FEF9E7",
        difficulty=1,
        phrases=[
            "Yellow sun.",
            "The color yellow.",
            "Yellow banana."
        ],
        sentences=[
            "The sun is yellow.",
            "Bananas are yellow.",
            "I see a yellow butterfly."
        ]
    )
    
    add_word(
        word="Purple",
        chinese="紫色",
        category="colors",
        emoji="🟣",
        color="#9B59B6",
        bg="F5EEF8",
        difficulty=1,
        phrases=[
            "Purple flower.",
            "The color purple.",
            "Purple grapes."
        ],
        sentences=[
            "Grapes can be purple.",
            "I like purple flowers.",
            "The butterfly has purple wings."
        ]
    )
    
    # 4. 形容词类
    add_word(
        word="Big",
        chinese="大的",
        category="adjectives",
        emoji="🐘",
        color="#3498DB",
        bg="EBF5FB",
        difficulty=1,
        phrases=[
            "A big dog.",
            "Big and small.",
            "It's big!"
        ],
        sentences=[
            "The elephant is very big.",
            "I have a big brother.",
            "This house is big!"
        ]
    )
    
    add_word(
        word="Small",
        chinese="小的",
        category="adjectives",
        emoji="🐭",
        color="#E74C3C",
        bg="FADBD8",
        difficulty=1,
        phrases=[
            "A small mouse.",
            "Small and cute.",
            "It's small."
        ],
        sentences=[
            "The mouse is very small.",
            "I have a small toy.",
            "Small things can be precious."
        ]
    )
    
    add_word(
        word="Tall",
        chinese="高的",
        category="adjectives",
        emoji="🦒",
        color="#2ECC71",
        bg="D5F5E3",
        difficulty=1,
        phrases=[
            "A tall tree.",
            "Tall and short.",
            "He is tall."
        ],
        sentences=[
            "The giraffe is very tall.",
            "My dad is tall.",
            "This building is tall!"
        ]
    )
    
    add_word(
        word="Short",
        chinese="矮的/短的",
        category="adjectives",
        emoji="🧸",
        color="#F39C12",
        bg="FEF9E7",
        difficulty=1,
        phrases=[
            "A short dog.",
            "Short and tall.",
            "It's short."
        ],
        sentences=[
            "The dog has short legs.",
            "This pencil is short.",
            "My little sister is short."
        ]
    )
    
    print("\n✅ 所有新单词添加完成！\n")
    
    # 打印更新后的单词列表
    print_word_list()

if __name__ == "__main__":
    add_all_new_words()
