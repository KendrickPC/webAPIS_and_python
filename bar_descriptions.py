import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome_python', 'system_design_primer', 'models']

plot_dicts = [
    {'value': 58818, 'label': 'Description of awesome_python'},
    {'value': 53618, 'label': 'Description of system_design_primer'},
    {'value': 46081, 'label': 'Description of models'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
