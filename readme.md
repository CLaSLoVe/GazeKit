# GazeKit (Under Development) 🚧👁️

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/your_username/GazeKit/blob/main/LICENSE)

**GazeKit** is a Python library currently under development for processing and analyzing eye-tracking data. It aims to provide a comprehensive set of functions for noise reduction, area of interest (AOI) localization, data analysis, and plotting. This library is being developed to simplify the preprocessing and analysis of eye-tracking data, enabling researchers in psychology, neuroscience, and human-computer interaction to gain valuable insights into human visual cognitive processes.

## Features

- **Noise Reduction:** GazeKit offers advanced techniques for reducing noise in eye-tracking data, allowing for more accurate and reliable analysis.
- **AOI Localization:** Easily define and locate areas of interest (AOIs) within eye-tracking data, facilitating the analysis of gaze patterns and attentional focus.
- **Data Analysis:** GazeKit provides a range of analysis tools, including fixation duration, saccade detection, heatmaps, and scanpath visualization, empowering researchers to extract meaningful information from eye-tracking data.
- **Plotting:** Visualize eye-tracking data with customizable plots and graphs, enabling researchers to effectively communicate their findings.

## Installation

Once GazeKit is released, you will be able to install it using `pip`:

```bash
pip install gazekit
```

## Usage

Once installed, you can use GazeKit in your Python code. Here's a sneak peek at how GazeKit might be used for preprocessing and analyzing eye-tracking data:

```python
import numpy as np
from gazekit.aoi import read_aoi_ini_file
from gazekit.sequence import Sequence

# Load eye-tracking data
data = np.genfromtxt('../tests/data.csv', delimiter=',', dtype=None, encoding=None)

# Load AOIs
aois = read_aoi_ini_file('../tests/aoi.ini', (2560, 1600))

# Load data into GazeKit Sequence class
seq = Sequence(*data.T)

# Apply noise reduction techniques (under development)
seq = seq.denoise(myfunc)

# Detect fixations (under development)
seq = seq.detect_fixations()

# Locate AOIs within the data
seq = seq.loc_aoi(aois)

# Generate a plot (under development)
heatmap = seq.plot(myfunc)

# ... Perform further analysis and visualization

```

For more detailed instructions and examples, please refer to the [documentation](https://github.com/your_username/GazeKit/wiki) (coming soon).

## Configuration

The `aoi.ini` file is a configuration file that defines areas of interest (AOIs) within the eye-tracking data. It has a format similar to the following:

```ini
[AI]
x = 880
y = 700
w = 430
h = 455
p = hi,tc
```

In the above example, `[AI]` is the name of the AOI. The `x`, `y`, `w`, and `h` parameters represent the starting point (x, y) and the width and height of the AOI, respectively. The `p` parameter represents the functionalities associated with the AOI and is specified as a list. In the example, `p = hi,tc` indicates that the AOI has functionalities for "hi" and "tc".

When using GazeKit, make sure that your eye-tracking data file includes columns for `x`, `y`, and `t` (time) information.

## Contributing

Contributions to GazeKit are welcome! Since this project is currently under development, we are not accepting contributions at this stage. However, once the project reaches a more stable state, we would love to collaborate with the open-source community. Stay tuned for updates!

## License

This project is licensed under the [MIT License](https://github.com/your_username/GazeKit/blob/main/LICENSE).

## Acknowledgements

We would like to express our gratitude to the open-source community for their valuable contributions and support in developing GazeKit. 🎉😊