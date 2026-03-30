#!/usr/bin/env python3
"""
添加家庭篇新单词：爷爷、奶奶、宝宝
"""

from word_list_manager import add_word, print_word_list

def add_family_words():
    """添加家庭篇新单词"""
    
    print("\n" + "="*60)
    print("📝 添加家庭篇新单词")
    print("="*60 + "\n")
    
    # 添加爷爷
    add_word(
        word="Grandpa",
        chinese="爷爷",
        category="family",
        emoji="👴",
        color="#3498DB",
        bg="EBF5FB",
        difficulty=1,
        phrases=[
            "My grandpa.",
            "Grandpa loves me.",
            "Grandpa is kind."
        ],
        sentences=[
            "Grandpa tells me stories.",
            "I love my grandpa very much.",
            "Grandpa has gray hair."
        ]
    )
    
    # 添加奶奶
    add_word(
        word="Grandma",
        chinese="奶奶",
        category="family",
        emoji="👵",
        color="#E91E63",
        bg="FCE4EC",
        difficulty=1,
        phrases=[
            "My grandma.",
            "Grandma is sweet.",
            "I love grandma."
        ],
        sentences=[
            "Grandma makes yummy cookies.",
            "My grandma is very kind.",
            "Grandma reads books to me."
        ]
    )
    
    # 添加宝宝
    add_word(
        word="Baby",
        chinese="宝宝",
        category="family",
        emoji="👶",
        color="#F39C12",
        bg="FEF9E7",
        difficulty=1,
        phrases=[
            "A cute baby.",
            "The baby is small.",
            "My baby brother."
        ],
        sentences=[
            "The baby is sleeping.",
            "Look at the cute baby!",
            "The baby cries when hungry."
        ]
    )
    
    print("\n✅ 家庭篇新单词添加完成！\n")
    
    # 打印更新后的单词列表
    print_word_list()

if __name__ == "__main__":
    add_family_words()
