# GazeKit (Under Development) 🚧👁️

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/your_username/GazeKit/blob/main/LICENSE)

**GazeKit** is a Python library currently under development for processing eye-tracking data. It aims to provide a comprehensive set of functions for noise reduction, area of interest (AOI) localization, data analysis, and plotting. This library is being developed to simplify the preprocessing and analysis of eye-tracking data, enabling researchers in psychology, neuroscience, and human-computer interaction to gain valuable insights into human visual cognitive processes.

## Features

- **Noise Reduction:** GazeKit will offer advanced techniques for reducing noise in eye-tracking data, allowing for more accurate and reliable analysis.
- **AOI Localization:** Easily define and locate areas of interest (AOIs) within eye-tracking data, facilitating the analysis of gaze patterns and attentional focus.
- **Data Analysis:** GazeKit will provide a range of analysis tools, including fixation duration, saccade detection, heatmaps, and scanpath visualization, empowering researchers to extract meaningful information from eye-tracking data.
- **Plotting:** Visualize eye-tracking data with customizable plots and graphs, enabling researchers to effectively communicate their findings.

## Installation

Once GazeKit is released, you will be able to install it using `pip`:

```bash
pip install gazekit
```

## Usage

Once installed, you will be able to use GazeKit in your Python code. Here's a sneak peek at how GazeKit might be used for preprocessing and analyzing eye-tracking data:

```python
import gazekit

# Load eye-tracking data
data = gazekit.load_data('path/to/data.csv')

# Apply noise reduction techniques
clean_data = gazekit.remove_noise(data)

# Define areas of interest (AOIs)
aois = gazekit.define_aois('path/to/aois.json')

# Locate AOIs within the data
aoi_data = gazekit.locate_aois(clean_data, aois)

# Calculate fixation duration
fixation_duration = gazekit.calculate_fixation_duration(aoi_data)

# Generate a heatmap
heatmap = gazekit.generate_heatmap(clean_data)

# Visualize scanpath
gazekit.plot_scanpath(clean_data)

# ... Perform further analysis and visualization

```

For more detailed instructions and examples, please refer to the [documentation](https://github.com/your_username/GazeKit/wiki) (coming soon).

## Contributing

Contributions to GazeKit are welcome! Since this project is currently under development, we are not accepting contributions at this stage. However, once the project reaches a more stable state, we would love to collaborate with the open-source community. Stay tuned for updates!

## License

This project is licensed under the [MIT License](https://github.com/your_username/GazeKit/blob/main/LICENSE).

## Acknowledgements

We would like to express our gratitude to the open-source community for their valuable contributions and support in developing GazeKit. 🎉😊