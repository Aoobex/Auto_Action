import cv2
from PIL import ImageGrab


def pipei(target):
    template = cv2.imread('action_finish.png')
    theight, twidth = template.shape[:2]
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    '''cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )'''
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return min_val
    strmin_val = str(min_val)  # min_val为结果，结果越小说明匹配越成功
    cv2.rectangle(target, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2)
    cv2.imshow("MatchResult----MatchingValue=" + strmin_val, target)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return min_val
