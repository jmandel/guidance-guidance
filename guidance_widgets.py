# guidance_widgets.py

from json import dumps
from IPython.display import display, Javascript
from ipywidgets import Button, HBox, VBox, Label, IntText, Text, Textarea, Layout

def create_form(inputs, run_func):
    input_widgets = []

    for key, value in inputs.items():
        if isinstance(value, str):
            widget = Textarea(value=value, layout=Layout(width="60%", height="10em"))
        else:
            widget = IntText(value=value, layout=Layout(width="3em"))

        label = Label(value=key, layout=Layout(width="200px"))
        input_widgets.append(HBox([label, widget]))

    run_button = Button(description="Run", button_style='success')

    def on_button_clicked(_b):
        kwargs = {widget.children[0].value: widget.children[1].value for widget in input_widgets}
        kwargs_json = dumps(kwargs)

        js_command = f"""
        var cell = IPython.notebook.insert_cell_below('code');
        cell.set_text('{run_func}(**{kwargs_json})');
        cell.execute();
        """
        display(Javascript(js_command))

    run_button.on_click(on_button_clicked)
    return VBox(input_widgets + [run_button])
