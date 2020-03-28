from main_gui import g


def output_writer(x):
    global g
    g.configure(state='normal')
    g.insert('end', f'{x}\n')
    g.configure(state='disabled')
