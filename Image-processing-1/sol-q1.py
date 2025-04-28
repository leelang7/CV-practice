from PIL import Image

def crop(img, coordinates):
    # TODO: [지시사항 1번] 이미지를 자르는 코드를 완성하세요.
    img_crop = img.crop(coordinates)
    
    return img_crop
    
def rotate(img, angle, expand=False):
    # TODO: [지시사항 2번] 이미지를 회전하는 코드를 완성하세요.
    img_rotate = img.rotate(angle, expand=expand)
    
    return img_rotate
    
def resize(img, new_size):
    # TODO: [지시사항 3번] 이미지 크기를 변경하는 코드를 완성하세요.
    img_resize = img.resize(new_size)
    
    return img_resize
    
def shearing(img, shear_factor):
    # TODO: [지시사항 4번] 이미지를 전단 변환하는 코드를 완성하세요.
    img_shearing = img.transform((int(img.size[0] * (1 + shear_factor)), img.size[1]),
                                 Image.Transform.AFFINE, (1, -shear_factor, 0, 0, 1, 0))
    
                                 
    return img_shearing
    
def show_image(img, name):
    img.save(name)


def main():
    img = Image.open("Lenna.png")
    
    # TODO: [지시사항 5번] 지시사항에 따라 적절한 이미지 변환을 수행하세요.
    img_crop = crop(img, (150, 200, 450, 300))
    img_rotate = rotate(img, 160, expand=True)
    img_resize = resize(img, (640, 360))
    img_shearing = shearing(img, 0.8)
    
    print("=" * 50, "Crop 결과", "=" * 50)
    show_image(img_crop, "crop.png")
    
    print("=" * 50, "Rotate 결과", "=" * 50)
    show_image(img_rotate, "rotate.png")
    
    print("=" * 50, "Resize 결과", "=" * 50)
    show_image(img_resize, "resize.png")
    
    print("=" * 50, "Shearing 결과", "=" * 50)
    show_image(img_shearing, "shearing.png")
    
    return img_crop, img_rotate, img_resize, img_shearing


if __name__ == "__main__":
    main()