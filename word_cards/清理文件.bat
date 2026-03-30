#!/bin/bash
# 清理无用文件脚本

echo "============================================================"
echo "🗑️  清理无用文件"
echo "============================================================"
echo ""

# 删除旧的脚本文件
echo "删除旧的脚本文件..."
rm -f create_beautiful_cards.py
rm -f create_final_cards.py
rm -f create_milk_image.py
rm -f create_practice.py
rm -f create_word_cards.py
rm -f create_word_with_images.py
rm -f create_yogurt_image.py
rm -f generate_images.py
rm -f add_new_words_example.py

# 删除旧的Word文档
echo "删除旧的Word文档..."
rm -f 英语单词卡片.docx
rm -f 英语单词卡片_完整版.docx
rm -f 英语短语和例句.docx
rm -f "~\$"*.docx

# 删除临时文件
echo "删除临时文件..."
rm -f ~\$*.docx

echo ""
echo "✅ 清理完成！"
echo ""
echo "============================================================"
echo "📁 保留的核心文件"
echo "============================================================"
echo ""
echo "【核心脚本】"
echo "  • word_database.json          - 单词数据库"
echo "  • word_list_manager.py        - 单词管理模块"
echo "  • generate_cards.py           - 生成标准卡片"
echo "  • generate_picture_cards.py   - 生成图片卡片 ⭐"
echo "  • generate_phrases_optimized.py - 生成短语例句"
echo "  • generate_interactive_quiz.py - 生成互动练习"
echo ""
echo "【学习文档】"
echo "  • 单词图片卡片.docx           - 图片卡片 ⭐ 新增"
echo "  • 英语单词卡片_自定义.docx    - 标准卡片"
echo "  • 英语短语和例句_优化版.docx  - 短语例句"
echo "  • 英语趣味互动练习.docx       - 互动练习"
echo "  • 英语单词趣味练习题.docx     - 练习题"
echo ""
echo "【说明文档】"
echo "  • README.md                   - 系统说明"
echo "  • 使用指南.md                 - 使用指南"
echo "  • 单词总览.md                 - 单词列表"
echo ""
echo "============================================================"
