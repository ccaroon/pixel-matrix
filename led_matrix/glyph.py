from led_matrix.glyphs import alpha_num


class Glyph:
    # data == [{"x", "y", "on"}]
    def __init__(self, data, width, height):
        self.__data = data
        self.width = width
        self.height = height

    def __iter__(self):
        return iter(self.__data)

    @classmethod
    def strlen(cls, msg: str, spacing=0):
        """Return length of the msg/str in LEDs"""
        # Assumes mono-spaced "font"
        glyph = Glyph.get(msg[0])

        return len(msg) * (glyph.width + spacing)

    @classmethod
    def get(cls, name):
        glyph_set = None
        glyph_name = str(name).upper()

        if glyph_name in alpha_num.DATA:
            glyph_set = alpha_num
        else:
            msg = f"Unknown Glyph: '{name}'"
            raise ValueError(msg)

        glyph_data = cls.__get_data(glyph_set.TEMPLATE, glyph_set.DATA.get(glyph_name))

        return Glyph(glyph_data, width=glyph_set.WIDTH, height=glyph_set.HEIGHT)

    @classmethod
    def __get_data(cls, template, pixels):
        data = []
        for idx, loc in enumerate(template):
            px_data = {"col": loc[1], "row": loc[0], "on": pixels[idx] == 1}

            data.append(px_data)

        return data
