#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文字處理工具集
提供各種實用的文字處理功能
"""

def reverse_text(text):
    """反轉文字"""
    return text[::-1]

def count_words(text):
    """計算單字數量"""
    return len(text.split())

def remove_spaces(text):
    """移除所有空格"""
    return text.replace(" ", "")

def capitalize_words(text):
    """將每個單字的第一個字母大寫"""
    return text.title()

def simple_encrypt(text, shift=3):
    """簡單的凱撒加密"""
    encrypted = ""
    for char in text:
        if char.isalpha():
            # 處理大小寫字母
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted += encrypted_char
        else:
            encrypted += char
    return encrypted

def simple_decrypt(text, shift=3):
    """簡單的凱撒解密"""
    return simple_encrypt(text, -shift)

def create_text_box(text, char="*"):
    """建立文字框"""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines) if lines else 0
    box_width = max_length + 4
    
    result = []
    result.append(char * box_width)
    
    for line in lines:
        padding = max_length - len(line)
        result.append(f"{char} {line}{' ' * padding} {char}")
    
    result.append(char * box_width)
    return '\n'.join(result)

# 示範使用
if __name__ == "__main__":
    sample_text = "Hello Python World"
    
    print(f"原始文字：{sample_text}")
    print(f"反轉文字：{reverse_text(sample_text)}")
    print(f"單字數量：{count_words(sample_text)}")
    print(f"移除空格：{remove_spaces(sample_text)}")
    print(f"標題格式：{capitalize_words(sample_text.lower())}")
    print(f"加密文字：{simple_encrypt(sample_text)}")
    
    print("\n文字框範例：")
    box_text = "歡迎學習Python\n字串處理很有趣"
    print(create_text_box(box_text, "#"))