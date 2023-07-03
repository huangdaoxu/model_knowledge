from model_knowledge.cv.ocr import ocr
from model_knowledge.pdf.image import extract_images


if __name__ == "__main__":
    images = extract_images(file='/Users/dawsonhuang/Downloads/330B88E8457B6271E628EDB2CB3_016E9BC2_1E7F67.pdf')
    for image in images:
        a = ocr(image)
        print(a)
