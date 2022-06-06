import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

def plot_visualization(isolated_data):
    graph_title = isolated_data.STUB_NAME.to_list()[0]
    x_axis = isolated_data.YEAR
    y_axis = isolated_data.ESTIMATE

    x_axis_tick_labels = isolated_data.YEAR.to_list()
    y_axis_tick_labels = isolated_data.ESTIMATE.to_list()

    plt.xlabel('Year')
    plt.ylabel('Percentage of Persons Who Delayed Care')

    plt.plot(x_axis, y_axis)
    panel_label = isolated_data.PANEL.to_list()[0]
    if 'medical' in panel_label:
        full_graph_title = 'Delay or Nonreceipt of Medical Care Due to Cost - ' + graph_title
    elif 'dental' in panel_label:
        full_graph_title = 'Delay or Nonreceipt of Dental Care Due to Cost - ' + graph_title
    elif 'drugs' in panel_label:
        full_graph_title = 'Delay or Nonreceipt of Prescription Drugs Due to Cost - ' + graph_title
    else:
        print('ya done goofed')
    plt.title(full_graph_title)

    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xticks(np.arange(min(x_axis_tick_labels), max(x_axis_tick_labels) + 1, 1))
    plt.xticks(rotation=45)

    plt.yticks(np.arange(min(y_axis_tick_labels)-1, max(y_axis_tick_labels) + 1, 0.25))

    plt.savefig(full_graph_title)
    plt.clf()
    return
