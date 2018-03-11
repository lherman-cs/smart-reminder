from PIL import Image
import numpy as np
import io

# Decode raw bytes png to numpy array array


def decode(raw_bytes):
    # stream = io.StringIO(raw_bytes)
    stream = io.BytesIO(raw_bytes)
    img = Image.open(stream)

    return np.array(img)
