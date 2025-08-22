#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
單位轉換工具
提供各種常用單位轉換功能
"""

import math

def temperature_conversions():
    """溫度轉換"""
    print("=== 溫度轉換器 ===")
    
    temp_type = input("選擇輸入溫度類型 (C=攝氏, F=華氏, K=開氏)：").upper()
    temp_value = float(input("請輸入溫度值："))
    
    if temp_type == 'C':
        celsius = temp_value
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
    elif temp_type == 'F':
        fahrenheit = temp_value
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
    elif temp_type == 'K':
        kelvin = temp_value
        celsius = kelvin - 273.15
        fahrenheit = celsius * 9/5 + 32
    else:
        print("無效的溫度類型！")
        return
    
    print(f"\n轉換結果：")
    print(f"攝氏：{celsius:.2f}°C")
    print(f"華氏：{fahrenheit:.2f}°F")
    print(f"開氏：{kelvin:.2f}K")

def distance_conversions():
    """距離轉換"""
    print("\n=== 距離轉換器 ===")
    
    meters = float(input("請輸入公尺數："))
    
    # 各種距離單位換算
    millimeters = meters * 1000
    centimeters = meters * 100
    kilometers = meters / 1000
    inches = meters * 39.3701
    feet = meters * 3.28084
    yards = meters * 1.09361
    miles = meters / 1609.34
    
    print(f"\n{meters}公尺等於：")
    print(f"毫米：{millimeters:,.2f} mm")
    print(f"公分：{centimeters:,.2f} cm")
    print(f"公里：{kilometers:,.4f} km")
    print(f"英寸：{inches:.2f} inches")
    print(f"英尺：{feet:.2f} feet")
    print(f"碼：{yards:.2f} yards")
    print(f"英里：{miles:.4f} miles")

def weight_conversions():
    """重量轉換"""
    print("\n=== 重量轉換器 ===")
    
    kg = float(input("請輸入公斤數："))
    
    # 各種重量單位換算
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    tons = kg / 1000
    
    print(f"\n{kg}公斤等於：")
    print(f"公克：{grams:,.2f} g")
    print(f"公噸：{tons:.4f} t")
    print(f"磅：{pounds:.2f} lbs")
    print(f"盎司：{ounces:.2f} oz")

def area_conversions():
    """面積轉換"""
    print("\n=== 面積轉換器 ===")
    
    square_meters = float(input("請輸入平方公尺數："))
    
    # 各種面積單位換算
    square_cm = square_meters * 10000
    square_km = square_meters / 1000000
    square_feet = square_meters * 10.7639
    square_inches = square_meters * 1550
    acres = square_meters / 4047
    hectares = square_meters / 10000
    
    print(f"\n{square_meters}平方公尺等於：")
    print(f"平方公分：{square_cm:,.2f} cm²")
    print(f"平方公里：{square_km:.6f} km²")
    print(f"平方英尺：{square_feet:.2f} ft²")
    print(f"平方英寸：{square_inches:.2f} in²")
    print(f"英畝：{acres:.4f} acres")
    print(f"公頃：{hectares:.4f} hectares")

def volume_conversions():
    """體積轉換"""
    print("\n=== 體積轉換器 ===")
    
    liters = float(input("請輸入公升數："))
    
    # 各種體積單位換算
    milliliters = liters * 1000
    cubic_meters = liters / 1000
    gallons_us = liters / 3.78541
    gallons_uk = liters / 4.54609
    fluid_ounces = liters * 33.814
    
    print(f"\n{liters}公升等於：")
    print(f"毫升：{milliliters:,.2f} ml")
    print(f"立方公尺：{cubic_meters:.4f} m³")
    print(f"美制加侖：{gallons_us:.2f} gal (US)")
    print(f"英制加侖：{gallons_uk:.2f} gal (UK)")
    print(f"液體盎司：{fluid_ounces:.2f} fl oz")

def currency_converter_demo():
    """貨幣轉換器示範（模擬匯率）"""
    print("\n=== 貨幣轉換器（示範版）===")
    
    # 模擬匯率（實際應用需要即時匯率API）
    exchange_rates = {
        'USD': 1.0,      # 美元基準
        'TWD': 31.5,     # 台幣
        'JPY': 110.0,    # 日圓
        'EUR': 0.85,     # 歐元
        'GBP': 0.73,     # 英鎊
        'CNY': 6.5,      # 人民幣
    }
    
    print("支援貨幣：USD, TWD, JPY, EUR, GBP, CNY")
    
    from_currency = input("輸入原幣別：").upper()
    to_currency = input("輸入目標幣別：").upper()
    amount = float(input("輸入金額："))
    
    if from_currency in exchange_rates and to_currency in exchange_rates:
        # 先轉換為USD，再轉換為目標貨幣
        usd_amount = amount / exchange_rates[from_currency]
        result = usd_amount * exchange_rates[to_currency]
        
        print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")
        print("注意：此為示範匯率，非實際匯率")
    else:
        print("不支援的貨幣類型！")

if __name__ == "__main__":
    print("單位轉換工具集")
    print("=" * 30)
    
    converters = [
        temperature_conversions,
        distance_conversions,
        weight_conversions,
        area_conversions,
        volume_conversions,
        currency_converter_demo
    ]
    
    for converter in converters:
        try:
            converter()
        except ValueError:
            print("輸入錯誤：請輸入有效的數字！")
        except Exception as e:
            print(f"發生錯誤：{e}")
        
        input("\n按Enter繼續...")
    
    print("所有轉換器演示完成！")