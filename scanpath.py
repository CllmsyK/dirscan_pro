# 该脚本可输出所有绝对路径
# gci后输入要输出的绝对路径目录
import os
def gci(filepath):
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    if os.path.isdir(fi_d):
      gci(fi_d)
    else:
      print(os.path.join(filepath,fi_d))
      
gci('C:\\phpstudy_pro\\WWW\\CmsEasy')
