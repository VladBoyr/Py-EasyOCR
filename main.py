import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image=file_path, detail=0)
    return result


def main():
    text = text_recognition(file_path="image.PNG")
    for line in text:
        print(line + '\n')


if __name__ == "__main__":
    main()
