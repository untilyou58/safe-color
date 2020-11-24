import cv2
import numpy as np

def get_hsv_colors_cv2(r, g, b):
  """HSVを計算する関数（OpenCVを使用）"""
  bgr = np.uint8([[[b, g, r ]]])
  hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
  h = hsv[0][0][0]
  s = hsv[0][0][1]
  v = hsv[0][0][2]
  h *= 2 # openCVでは0-180のため
  return h, s, v

def get_complementary_colors(r, g, b):
  """補色を計算する関数"""
  tmp = max(r, g, b) + min(r, g, b)
  return tmp - r, tmp - g, tmp - b

def get_opposite_colors(r, g, b):
  """反対色を計算する関数"""
  return 255 - r, 255 - g, 255 - b

def get_hsv_colors(r, g, b):
  """
  HSVを計算する関
  円柱モデルを使用
  h, s, vの取りうる値の範囲は
  h : 0 - 360
  s : 0 - 255
  v : 0 - 255
  とした
  """
  r /= 255
  g /= 255
  b /= 255
  max_rgb = max(r, g, b)
  min_rgb = min(r, g, b)
  v = max_rgb
  if v == 0 or v == min_rgb:
    h = 0
    s = 0
  else:
    s = (max_rgb - min_rgb) / max_rgb
    if min_rgb == b:
      h = 60 * (g - r)/(max_rgb - min_rgb) + 60
    elif min_rgb == r:
      h = 60 * (b - g)/(max_rgb - min_rgb) + 180
    elif min_rgb == g:
      h = 60 * (r - b)/(max_rgb - min_rgb) + 300
  h %= 360
  s *= 255
  v *= 255
  return int(h), int(s), int(v)

print('| カラーコード | $(R, G, B)$ | $(H, S, V)$ | 補色 | 反対色 |')
print('| :---: | :--- | :--- | :---: | :---: |')
for r in range(0, 256, 51):
  for g in range(0, 256, 51):
    for b in range(0, 256, 51):
      r_c, g_c, b_c = get_complementary_colors(r, g, b)
      r_o, g_o, b_o = get_opposite_colors(r, g, b)
      h, s, v = get_hsv_colors(r, g, b)
      color_code = '`#' + format(r, '02x') + format(g, '02x') + format(b, '02x') + '`' # 16進数に変換
      rgb = '$({}, {}, {})$'.format(r, g, b)
      hsv = '$({}, {}, {})$'.format(h, s, v)
      color_code_comp = '`#' + format(r_c, '02x') + format(g_c, '02x') + format(b_c, '02x') + '`'
      color_code_opposit = '`#' + format(r_o, '02x') + format(g_o, '02x') + format(b_o, '02x') + '`'
      print('| {} | {} | {} | {} | {} |'.format(color_code, rgb, hsv, color_code_comp, color_code_opposit))
