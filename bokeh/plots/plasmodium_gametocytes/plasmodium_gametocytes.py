import os

import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import gridplot, layout
from bokeh.models import Tabs, Panel
from bokeh.models.sources import ColumnDataSource

from scripts.all_rpkm_plot import all_rpkm_plot
from scripts.rpkm_plot import rpkm_plot

# data_dir = os.path.abspath('../data')

# Note - needs to be relative to where the server runs from.
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

data = pd.read_csv(f"{data_dir}/umap_data.tab", sep="\t")
rpkm_data = pd.read_csv(f"{data_dir}/rpkm_data_umap_coords", sep="\t")
all_genes_rpkm = pd.read_csv(f"{data_dir}/all_genes_umap", sep="\t")
rpkm_data_mean_stddev = pd.read_csv(
    f"{data_dir}/rpkm_data_mean_stddev", sep="\t", index_col=[0, 1, 2]
)

gene_list = all_genes_rpkm.gene_id.to_list()

rpkm_p = rpkm_plot(data, rpkm_data, rpkm_data_mean_stddev, gene_list)
all_rpkm_p = all_rpkm_plot(all_genes_rpkm, gene_list)

tabs = Tabs(tabs=[
    Panel(child=all_rpkm_p, title="Samples Plot"), 
    Panel(child=rpkm_p, title="Genes Plot"),    
    ])

    
# , rpkm_p


# Bokeh func to serve the charts.
curdoc().add_root(tabs)
