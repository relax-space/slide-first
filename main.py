'''
计算滑块移动距离: 通过两个图形匹配, 来计算缺口的x轴
'''

from typing import Tuple

import cv2


def get_loc(bg_img_path: str, gp_img_path: str) -> Tuple[int, int]:
    bg_1 = cv2.imread(bg_img_path)
    gp_1 = cv2.imread(gp_img_path)
    cv2.imwrite('out/bg_1.jpg', bg_1)
    cv2.imwrite('out/gp_1.png', gp_1)

    #
    bg_2 = cv2.Canny(bg_1, 100, 200)
    gp_2 = cv2.Canny(gp_1, 100, 200)
    cv2.imwrite('out/bg_2.png', bg_2)
    cv2.imwrite('out/gp_2.png', gp_2)

    res = cv2.matchTemplate(bg_2, gp_2, cv2.TM_CCORR_NORMED)
    _, _, _, loc = cv2.minMaxLoc(res)
    return loc


def print_res(loc: Tuple[int, int], out_img_path: str, bg_img_path: str,
              gp_img_path: str):
    x, y = loc
    bg_img = cv2.imread(bg_img_path)
    gp_img = cv2.imread(gp_img_path)
    height, width, _ = gp_img.shape
    loc2 = (x + width, y + height)
    cv2.rectangle(bg_img, loc, loc2, (0, 0, 255), 1)
    cv2.imwrite(out_img_path, bg_img)


bg = 'asset/1.jpg'
gp = 'asset/1.png'
out = 'out/res_1.jpg'
loc = get_loc(bg, gp)

print_res(loc, out, bg, gp)
