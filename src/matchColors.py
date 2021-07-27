from src.colors import myColors
import config


def returnMatchedColors():
    if isinstance(config.color, str):
        color = getattr(myColors, config.color)
    else:
        color = config.color

    if isinstance(config.background_color, str):
        background_color = getattr(myColors, config.background_color)
    else:
        background_color = config.background_color

    return color, background_color
