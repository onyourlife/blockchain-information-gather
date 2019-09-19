#!/usr/bin/python3
# -*- coding: utf-8 -*-

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

def setFont(cell):
    cell.font = Font(name='맑은 고딕', size=10, bold=True)

def setAlign(cell):
    cell.alignment = Alignment(horizontal='center', vertical='center')

wb = Workbook()
ws = wb.active
ws.freeze_panes = 'A3'

title = ['A3','B3','C3','D3','E3']
title_content = ['ID', 'NAME', 'ICO 시작일', 'ICO 종료일', 'ICO 총 상장액']
ws.merge_cells('A1:E1')

for i in range(len(title)):
    ws[title[i]] = title_content[i]

for i in range(len(title)):
    setFont(ws[title[i]])

for i in range(len(title)):
    setAlign(ws[title[i]])

wb.save('test.xlsx')

