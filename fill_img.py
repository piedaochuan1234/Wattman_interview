import json
import cv2


def read_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as js_file:
        json_dict = json.load(js_file)
        return json_dict


def fillBbox(img_target, img_fill, bbox, keepRatio: bool):
    """
    given bbox, fill source image into target image

    :param img_target: target image to fill
    :param img_fill: source image to fill
    :param bbox: [xmin,ymin,xmax,ymax]
    :param keepRatio: whether keep ratio
    :return: result image
    """
    imgFillH, imgFillW = img_fill.shape[0:2]

    xmin, ymin, xmax, ymax = bbox
    bboxW = xmax - xmin
    bboxH = ymax - ymin

    # get opencv interpolation method
    cv_inter = cv2.INTER_NEAREST
    if imgFillH < bboxH and imgFillW < bboxW:
        cv_inter = cv2.INTER_LINEAR
    elif imgFillH > bboxH and imgFillW > bboxW:
        cv_inter = cv2.INTER_AREA

    if keepRatio:

        ratio = min(bboxW / imgFillW, bboxH / imgFillH)
        newW = int(imgFillW * ratio)
        newH = int(imgFillH * ratio)
        # print('ratio: ',ratio)
        # print("newH: {}, newW: {}".format(newH,newW))
        img_fill = cv2.resize(img_fill, (newW, newH), interpolation=cv_inter)
        dx = (bboxW - newW) // 2
        dy = (bboxH - newH) // 2
        img_resize = cv2.copyMakeBorder(img_fill, dy, dy, dx, dx, cv2.BORDER_CONSTANT, value=(114, 114, 114))
        # print('img_resize shape: ',img_resize.shape)
    else:

        img_resize = cv2.resize(img_fill, (bboxW, bboxH), interpolation=cv_inter)

    img_target[ymin:ymax, xmin:xmax] = img_resize

    return img_target


if __name__ == '__main__':
    imgFill_path = './data/images/fill.jpg'
    imgTarget_path = './data/images/target.jpg'
    js_path = 'data/jsons/boxes.json'
    keepRatio = False
    # keepRatio = True

    img_fill = cv2.imread(imgFill_path)
    img_target = cv2.imread(imgTarget_path)
    json_dict = read_json(js_path)

    bbox_info = json_dict['boxes'][1]['rectangle']
    print('box_b rectangle , info: ', bbox_info)

    xmin, ymin = bbox_info['left_top']
    xmax, ymax = bbox_info['right_bottom']
    bbox = [xmin, ymin, xmax, ymax]

    img_res = fillBbox(img_target, img_fill, bbox, keepRatio)

    cv2.imshow("img_res", img_res)
    cv2.waitKey(0)
