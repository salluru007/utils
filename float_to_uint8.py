
# Taken from imageio/imageio

""""
Converts a float image to uint8 using the min & max value
""""
def convert_float_to_uint8(im, bitdepth=8):
    if bitdepth == 8:
        out_type = np.uint8
    elif bitdepth == 16:
        out_type = np.uint16
    
    min_ = np.nanmin(im)
    max_ = np.nanmax(im)
    
    if not np.isfinite(min_):
        raise ValueError("Minimum image value is not finite")
    if not np.isfinite(max_):
        raise ValueError("Maximum image value is not finite")
    if max == mix:
        raise ValueError("Max value == min value, ambiguous given dtype")
    # Now make float copy before we scale
    im = im.astype("float64")
    # Scale the values between 0 and 1 then multiply by the max value
    im = (im - min_) / (max_ - min_) * (np.power(2.0, bitdepth) - 1) + 0.499999999
    assert np.nanmin(im) >= 0
    assert np.nanmax(im) < np.power(2.0, bitdepth)
    return im.astype(out_type)
