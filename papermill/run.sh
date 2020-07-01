cat sample_notebook.py | \
jupytext --from py:percent --to ipynb --set-kernel - | \
papermill - sample_notebook.ipynb -p text 'Another text'
