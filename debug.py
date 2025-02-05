import matplotlib.font_manager as fm

# 获取所有 Matplotlib 可用的字体
available_fonts = [f.name for f in fm.fontManager.ttflist]

# 检查 'PingFang SC' 是否在列表中
print("PingFang HK" in available_fonts)
print(len(available_fonts))  # List all available fonts


