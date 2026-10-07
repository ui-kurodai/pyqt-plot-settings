# pyqt-plot-settings

PyQt6 data models and a dialog for editing Matplotlib-style plot settings.
The package does not render plots or depend on Matplotlib. The caller applies
the settings to its own plotting code.

## Development

```powershell
python -m pip install -e .
python examples/basic.py
```

With uv, use `uv run python examples/basic.py`.

## Usage

```python
from pyqt_plot_settings import (
    PlotSettingsDialog, SeriesPlotSettings, SharedPlotSettings,
)

settings = SharedPlotSettings(x_label="X", y_label="Y")
dialog = PlotSettingsDialog(settings, [SeriesPlotSettings("Data")], parent=parent)
dialog.applied.connect(redraw)
if dialog.exec():
    redraw()
```

Create a QApplication before constructing the dialog. `redraw` and `parent`
are supplied by the application.

## Settings contract

- The dialog edits the supplied settings object in place.
- Apply reads the form, records a snapshot, and emits `applied` with no arguments.
- OK reads the form and accepts the dialog; it does not emit `applied`.
- Cancel restores the latest Apply snapshot, or the initial snapshot if Apply
  has not been used. Nested settings objects may be replaced during restoration.
- Construction reconciles series, extra axes, and annotations with the supplied
  defaults before recording the initial snapshot. Entries absent from those
  defaults are removed (manual series are retained).
- Series labels also serve as keys; use unique labels.
- Figure sizes and padding are in inches. Annotation and coordinate legend
  positions are axes-relative. Digit count -1 means automatic formatting;
  tick count 0 means automatic ticks. Bounds of None mean automatic limits.
- Colors, styles, colormap names, and legend locations use Matplotlib conventions.
  Formula evaluation, parsing manual coordinates, drawing, and plot-specific
  validation belong to the caller.

This initial extraction preserves the original dialog behavior and Python 3.12
requirement. The SHG measurement application consumes this package as an editable local dependency.

## Distribution

The project uses a src layout and a setuptools build backend. It can be installed
from a local directory or a Git repository after publishing. Pin a release tag or
commit when consuming it from Git.

A redistribution license must be selected by the owner before public release;
this initial extraction does not assign a license.
