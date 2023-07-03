from model_knowledge.cv.ocr import ocr
from model_knowledge.pdf.image import extract_images


if __name__ == "__main__":
    images = extract_images(file='./example.pdf')
    for image in images:
        a = ocr(image)
        print(a)
