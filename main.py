import voice_recognizer as vr


def main():
    print('Initializing....')
    text = vr.from_mic()

    if text is not None:
        print('Identified text : ' + text)

    else:
        print('returned variable is empty or null')


main()
