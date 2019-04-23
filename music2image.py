class Music2Image(object):

    def __init__(self):
        pass

    @staticmethod
    def _normalize_frequency(note):
        return note / 87

    @staticmethod
    def _freq2hue(note_normalized):
        return int(note_normalized * 180)

    @staticmethod
    def amp2value(amplitude_normalized):
        return int(amplitude_normalized * 255)

    @staticmethod
    def calc_saturation(hue, value):
        return int(np.sqrt(hue * value) * 255)


if __name__ == '__main__':
    print(1)