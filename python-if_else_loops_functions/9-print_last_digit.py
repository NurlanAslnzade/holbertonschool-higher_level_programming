#!/usr/bin/python3
def print_last_digit(number):
    """
    Verilmiş ədədin son rəqəmini hesablayır, çap edir və qaytarır.
    
    Args:
        number (int): Son rəqəmi tapılacaq tam ədəd.
        
    Returns:
        int: Ədədin son rəqəminin mütləq dəyəri.
    """
    # 1. Ədədin mütləq dəyərini tapırıq (abs(number)), 
    # çünki çıxış nümunəsində mənfi ədədlərin son rəqəmi də müsbət çap edilir (məsələn, -1024 üçün 4).
    # 2. Modulus (%) operatoru ilə son rəqəmi çıxarırıq.
    last_digit = abs(number) % 10
    
    # Son rəqəmi çap edirik (yeni sətir olmadan, çünki main.py hər şeyi bir sətirdə birləşdirir)
    print(last_digit, end="")
    
    # Son rəqəmin dəyərini qaytarırıq
    return last_digit
