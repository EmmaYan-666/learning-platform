# 🌟 英语单词卡片生成系统

> 为5岁儿童量身定制的英语学习卡片系统，支持持续更新和扩展

## ✨ 系统特点

- ✅ **智能管理** - 自动管理单词数据库
- ✅ **精美卡片** - 生成可打印的Word格式卡片
- ✅ **丰富内容** - 每个单词配有短语和例句
- ✅ **分类清晰** - 按主题分类，便于学习
- ✅ **持续更新** - 随时添加新单词

## 📦 当前包含

### 单词数量：35个

**分类统计：**
- 🐾 动物篇 (ANIMALS): 9个
- 🍎 食物篇 (FOOD): 12个
- 👨‍👩‍👧 家庭篇 (FAMILY): 2个
- 🎨 颜色篇 (COLORS): 8个
- 📏 形容词篇 (ADJECTIVES): 4个

## 📚 生成的文档

### 1. 英语单词卡片_自定义.docx
- 35张精美单词卡片
- 每张包含：图片/emoji + 英文单词 + 中文翻译
- 统一尺寸，方便打印和剪裁
- 彩色边框设计

### 2. 英语短语和例句.docx
- 每个单词3个简单短语
- 每个单词3个实用例句
- 按类别分组展示
- 适合家长辅导使用

### 3. 英语单词趣味练习题.docx
- 连线题（8题）
- 选择题（5题）
- 填空题（8题）
- 分类游戏
- 配套答案

## 🚀 快速使用

### 查看所有单词
```bash
python3 word_list_manager.py
```

### 生成卡片
```bash
python3 generate_cards.py
```

### 添加新单词
```python
from word_list_manager import add_word

add_word(
    word="Book",
    chinese="书",
    category="objects",
    emoji="📚",
    color="#3498DB",
    bg="EBF5FB",
    difficulty=1,
    phrases=["A big book.", "Read a book.", "My book."],
    sentences=["I like reading books.", "This book is interesting.", "Let's read a book together!"]
)
```

## 📁 文件结构

```
word_cards/
├── word_database.json              # 单词数据库
├── word_list_manager.py            # 管理模块
├── generate_cards.py               # 卡片生成
├── add_all_new_words.py            # 批量添加示例
├── images/                         # 自定义图片
│   ├── milk.png
│   └── yogurt.png
├── 英语单词卡片_自定义.docx         # 卡片文档
├── 英语短语和例句.docx             # 短语例句
├── 英语单词趣味练习题.docx         # 练习题
├── 单词总览.md                     # 单词列表
└── 使用指南.md                     # 详细说明
```

## 💡 学习建议

### 每日学习计划
1. **早晨** - 复习昨天学过的单词（5分钟）
2. **白天** - 学习3-5个新单词（10分钟）
3. **晚上** - 使用卡片游戏巩固（10分钟）

### 学习方法
- 📖 **看图说单词** - 指着卡片，大声说出英文
- 🎯 **听音找图** - 家长读单词，孩子找卡片
- 🎲 **卡片游戏** - 配对、记忆、分类游戏
- 💬 **情景对话** - 使用短语和例句练习
- 🏠 **生活应用** - 在生活中找到并说出单词

### 学习进度
- **第1-2周**: 基础词汇（动物、水果、基础颜色）
- **第3-4周**: 扩展词汇（更多食物、颜色）
- **第5-6周**: 形容词学习（大小、高矮）
- **第7-8周**: 综合应用和练习题

## 🎯 下一步计划

### 建议添加的单词类别

**数字篇 (NUMBERS)**
- One, Two, Three, Four, Five
- Six, Seven, Eight, Nine, Ten

**身体部位 (BODY)**
- Head, Hand, Foot, Eye, Ear, Nose, Mouth

**日常物品 (OBJECTS)**
- Book, Pen, Ball, Toy, Chair, Table

**动作篇 (ACTIONS)**
- Run, Jump, Walk, Eat, Drink, Sleep

**自然篇 (NATURE)**
- Sun, Moon, Star, Flower, Tree, Rain

## 🔄 更新日志

### 2026-03-18
- ✅ 初始版本发布（13个单词）
- ✅ 添加食物类：Watermelon, Water, Rice
- ✅ 添加动物类：Monkey
- ✅ 新增颜色篇：Red, Green, Blue, White, Black, Brown, Yellow, Purple
- ✅ 新增形容词篇：Big, Small, Tall, Short
- ✅ 总计35个单词
- ✅ 生成配套练习题

## 📞 技术支持

详细使用说明请查看：
- `使用指南.md` - 完整操作指南
- `单词总览.md` - 单词列表和学习建议

## 📄 许可

本系统仅供教育和学习使用。

---

**让英语学习变得有趣而高效！** 🎉
