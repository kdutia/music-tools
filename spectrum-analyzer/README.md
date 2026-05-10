# Audio Spectrum Analyzer

A browser-based audio spectrum analyzer that processes WAV files to create spectrograms and identify prominent frequencies. Perfect for designing musical scales around the harmonic content of recordings.

## Features

- **Spectrogram Visualization**: Visual representation of frequency content over time
- **Prominent Frequency Detection**: Automatically identifies and ranks the most significant frequencies
- **Adjustable Parameters**: Control the number of peaks detected and threshold sensitivity
- **No Dependencies**: Pure vanilla JavaScript, HTML, and CSS - no frameworks required
- **GitHub Pages Compatible**: Static files ready to host anywhere

## How It Works

1. **Upload**: Select a WAV audio file using the file picker
2. **Analysis**: The app uses the Web Audio API to decode the audio
3. **FFT Processing**: Performs Fast Fourier Transform with 4096-point resolution for detailed frequency analysis
4. **Spectrogram Generation**: Creates a time-frequency representation with color-coded intensity
5. **Peak Detection**: Identifies local maxima in the averaged frequency spectrum
6. **Results**: Displays prominent frequencies sorted by magnitude

## Usage

1. Open `index.html` in a modern web browser
2. Click "Choose WAV File" and select your audio file
3. Wait for the analysis to complete
4. View the spectrogram and prominent frequencies
5. Adjust controls:
   - **Number of peaks**: How many frequencies to display (1-50)
   - **Threshold**: Minimum relative magnitude for peak detection (0-1)

## Technical Details

- **FFT Size**: 4096 samples (high frequency resolution)
- **Window Function**: Hanning window to reduce spectral leakage
- **Algorithm**: Cooley-Tukey iterative FFT implementation
- **Peak Detection**: Local maxima detection with configurable threshold
- **Visualization**: Logarithmic dB scale with HSL color mapping (blue=quiet, red=loud)

## Use Cases

- Designing musical scales based on recorded sounds
- Analyzing the harmonic content of instruments
- Finding resonant frequencies in acoustic spaces
- Educational purposes for understanding audio spectra
- Sound design and synthesis reference

## Browser Compatibility

Requires a modern browser with Web Audio API support:
- Chrome 14+
- Firefox 25+
- Safari 6+
- Edge (all versions)

## Hosting on GitHub Pages

1. Push this directory to a GitHub repository
2. Go to repository Settings > Pages
3. Select the branch and folder containing `index.html`
4. Your analyzer will be live at `https://username.github.io/repository-name/`

## License

Free to use and modify for any purpose.
