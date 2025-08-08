import panel as pn
from eda import eda_dashboard
from analysis import analysis_dashboard

class Dashboard:
    def __init__(self):
        pn.extension()

        # Add tabs
        self.tabs = pn.Tabs(
            ("Exploring the Data", eda_dashboard),
            ("In Depth Analysis", analysis_dashboard),
            sizing_mode="stretch_both"
        )

    def show(self):
        return self.tabs