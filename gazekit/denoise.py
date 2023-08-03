from scipy import signal


def XXXMethod(x, y, t, window_size=5, polyorder=3):

    # Apply Savitzky-Golay filter to x and y coordinates separately
    x_filt = signal.savgol_filter(x, window_size, polyorder)
    y_filt = signal.savgol_filter(y, window_size, polyorder)

    # Create a new DataFrame with denoised x and y coordinates
    return (x_filt, y_filt, t)