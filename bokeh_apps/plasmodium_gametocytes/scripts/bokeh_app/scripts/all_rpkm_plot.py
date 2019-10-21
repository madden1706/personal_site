import numpy as np
import pandas as pd
from bokeh.layouts import column, gridplot, layout, widgetbox
from bokeh.models import ColorBar, CustomJS, HoverTool, LinearColorMapper, Panel
from bokeh.models.sources import ColumnDataSource
from bokeh.models.widgets import (
    CheckboxGroup,
    DataTable,
    DateFormatter,
    Select,
    TableColumn,
    TextInput,
)
from bokeh.plotting import figure


def all_rpkm_plot(data):
    def make_dataset(sample1, sample2):
        """Get data. Return a ColumnDataSource"""
        temp1 = data.loc[:, [sample1, sample2, "x", "y", "gene_id"]]
        temp1.loc[:, "sample1_val"] = temp1.loc[:, f"{sample1}"]
        temp1.loc[:, "sample2_val"] = temp1.loc[:, f"{sample2}"]
        sample_data = ColumnDataSource(temp1)

        return sample_data

    def make_highlight_dataset(gene):
        return ColumnDataSource(data[data["gene_id"] == f"{gene}"])

    sample_list = data.columns.tolist()
    sample_list.remove("x")
    sample_list.remove("y")
    sample_list.remove("gene_id")

    sample1 = Select(
        title="Sample 1:", value="30h_1 Rapamycin (SRX365318)", options=sample_list
    )
    sample2 = Select(
        title="Sample 2:", value="30h_1 No Rapamycin (SRX365318)", options=sample_list
    )
    sample_data = make_dataset(sample1.value, sample2.value)

    def make_plot(sample_data, highlight_data):

        # Plot tools
        base_plot_options = dict(
            width=550,
            plot_height=550,
            tools=["box_select, pan, wheel_zoom, box_zoom, reset"],
        )

        hover_gene_id = HoverTool(tooltips=[("Gene ID", "@gene_id")])

        plot_options = base_plot_options
        plot_options["tools"].append(hover_gene_id)

        # Range the covers 5 - 95 %iles.
        max_c = 10
        min_c = -1
        mapper = LinearColorMapper(palette="Plasma256", low=min_c, high=max_c)

        p1 = figure(**plot_options, title="Sample 1")  # title=f'{sample1.value}')
        p1.circle(
            "x",
            "y",
            size=7,
            source=sample_data,
            fill_color={"field": "sample1_val", "transform": mapper},
            line_color="grey",
        )
        # Sample highlight
        p1.circle(
            "x",
            "y",
            source=highlight_data,
            fill_alpha=0,
            line_color="#292929",
            line_width=1.5,
            size=12,
        )
        p1.text(
            "x",
            "y",
            source=highlight_data,
            text="gene_id",
            x_offset=4,
            y_offset=-3,
            text_color="#292929",
            text_font_size="9pt",
        )

        p2 = figure(**plot_options, title="Sample 2")
        p2.circle(
            "x",
            "y",
            size=7,
            source=sample_data,
            fill_color={"field": "sample2_val", "transform": mapper},
            line_color="grey",
        )
        # Sample highlight
        p2.circle(
            "x",
            "y",
            source=highlight_data,
            fill_alpha=0,
            line_color="#292929",
            line_width=1.5,
            size=12,
        )
        p2.text(
            "x",
            "y",
            source=highlight_data,
            text="gene_id",
            x_offset=4,
            y_offset=-3,
            text_color="#292929",
            text_font_size="9pt",
        )

        color_bar = ColorBar(color_mapper=mapper, width=8, location=(0, 0))
        p2.add_layout(color_bar, "left")

        p1.x_range = p2.x_range
        p1.y_range = p2.y_range

        p1.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        p1.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
        p1.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        p1.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
        p1.xaxis.major_label_text_font_size = (
            "0pt"
        )  # preferred method for removing tick labels
        p1.yaxis.major_label_text_font_size = (
            "0pt"
        )  # preferred method for removing tick labels
        p1.xaxis.axis_label = "UMAP1"
        p1.yaxis.axis_label = "UMAP2"

        p2.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        p2.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
        p2.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        p2.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks
        p2.xaxis.major_label_text_font_size = (
            "0pt"
        )  # preferred method for removing tick labels
        p2.yaxis.major_label_text_font_size = (
            "0pt"
        )  # preferred method for removing tick labels
        p2.xaxis.axis_label = "UMAP1"
        p2.yaxis.axis_label = "UMAP2"

        # Datatable
        selected_data = ColumnDataSource(
            data=dict(gene_id=[], sample1_val=[], sample2_val=[], fold_change=[])
        )  # x=[], y=[]))

        # Returns selected values - but also others - empty, just the gene_id

        sample_data.selected.js_on_change(
            "indices",
            CustomJS(
                args=dict(s1=sample_data, s2=selected_data),
                code="""
            setTimeout(function(){

                var inds = cb_obj.indices;
                var d1 = s1.data;
                var d2 = s2.data;
                d2['sample1_val'] = []
                d2['sample2_val'] = []
                // d2['x'] = []
                // d2['y'] = []
                d2['gene_id'] = []
                d2['fold_change'] = []
                
                for (var i = 0; i < inds.length; i++) {
                    if(d1['sample1_val'][inds[i]] != null){
                        d2['sample1_val'].push(d1['sample1_val'][inds[i]])
                        d2['sample2_val'].push(d1['sample2_val'][inds[i]])
                        d2['gene_id'].push(d1['gene_id'][inds[i]])
                        //d2['fold_change'].push(d1['sample1_val'][inds[i]])
                        var fc = Math.abs(d1['sample1_val'][inds[i]] / d1['sample2_val'][inds[i]]); 
                        d2['fold_change'].push(fc)
                       // d2['x'].push(d1['x'][inds[i]])
                       // d2['y'].push(d1['y'][inds[i]])

                    }
                }
                s2.change.emit();
            
            }, 1500); 
            """,
            ),
        )

        columns = [
            TableColumn(field="gene_id", title="Gene ID"),
            TableColumn(field="sample1_val", title="Sample 1 logRPKM"),
            TableColumn(field="sample2_val", title="Sample 2 logRPKM"),
            TableColumn(field="fold_change", title="Fold Change"),
            # TableColumn(field="x", title="X",),
            # TableColumn(field="y", title="Y"),
        ]

        data_table = DataTable(
            source=selected_data, columns=columns, width=500, height=300
        )

        # final_plot = layout([[p1, p2]])

        # final_plot = gridplot(
        #     children=[[sample1, sample2], [p1, p2]],
        #     toolbar_location='above',
        #     sizing_mode='fixed',
        # )

        return p1, p2, data_table

    # Samples check list
    sample_list = sorted(data.columns.tolist())
    sample_list.remove("x")
    sample_list.remove("y")
    sample_list.remove("gene_id")

    # Gene finder tool
    text_input = TextInput(value="PBANKA_1106000", title="Find Gene ID:")

    sample1 = Select(
        title="Sample 1 selection:",
        value="30h_1 Rapamycin (SRX365318)",
        options=sample_list,
    )
    sample2 = Select(
        title="Sample 2 selection:",
        value="30h_1 No Rapamycin (SRX365318)",
        options=sample_list,
    )
    sample_data = make_dataset(sample1.value, sample2.value)
    highlight_data = make_highlight_dataset(text_input.value)

    def update(attr, old, new):
        new_data = make_dataset(sample1.value, sample2.value)
        # sample1_data.data.update(new_data1.data)
        sample_data.data = new_data.data

        if text_input.value in data["gene_id"].unique().tolist():
            new_highlight = make_highlight_dataset(text_input.value)
            highlight_data.data = new_highlight.data
        else:
            new_highlight = make_highlight_dataset("")
            highlight_data.data = new_highlight.data

        # print(sample1_data.data.keys())

    plot1, plot2, data_table = make_plot(sample_data, highlight_data)
    widgets = layout([[sample1, sample2], [text_input]])
    final = gridplot([[plot1, plot2], [widgets, data_table]])
    final_tab = Panel(child=final, title="Genes Plot")
    sample1.on_change("value", update)
    sample2.on_change("value", update)
    text_input.on_change("value", update)

    # def callback(attr, old, new):
    #     print(new)

    # sample_data.data_source.on_change('selected',callback)

    return final_tab

    # TODO - slider for RPKM val.
    # TODO rename samples. Use mean?
