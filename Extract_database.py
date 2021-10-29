import os
import pyunpack

os.makedirs("static", exist_ok=True)
pyunpack.Archive("imgnew.rar").extractall('static')
