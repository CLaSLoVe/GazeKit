from scipy import signal
from sequence import Sequence


def XXXMethod(seq: Sequence, window_size=5, polyorder=3) -> Sequence:

    # Apply Savitzky-Golay filter to x and y coordinates separately
    x_filt = signal.savgol_filter(seq.data['x'], window_size, polyorder)
    y_filt = signal.savgol_filter(seq.data['y'], window_size, polyorder)

    # Create a new DataFrame with denoised x and y coordinates
    return Sequence(x_filt, y_filt, seq.data['t'])