"""Run with: python examples/basic.py (after installing the package)."""
import sys
from PyQt6.QtWidgets import QApplication
from pyqt_plot_settings import PlotSettingsDialog, SeriesPlotSettings, SharedPlotSettings


def main():
    app = QApplication(sys.argv)
    settings = SharedPlotSettings(title="Example", x_label="X", y_label="Y")
    dialog = PlotSettingsDialog(
        settings,
        [SeriesPlotSettings("Data", "C0", "o"), SeriesPlotSettings("Fit", "C1", "-")],
    )
    dialog.applied.connect(lambda: print("Applied:", settings))
    result = dialog.exec()
    print("Accepted:" if result else "Cancelled:", settings)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
