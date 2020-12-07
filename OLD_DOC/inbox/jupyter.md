# Jupyter Commands

#### Pandas & Jupyter


#### Export Using nbconvert

```python
jupyter nbconvert \
  --to html \
  --output jupyter_output.html \
  --TagRemovePreprocessor.remove_input_tags={\"rm_input", } \
  --TagRemovePreprocessor.remove_all_outputs_tags={\"rm_output", } \
  --TagRemovePreprocessor.remove_cell_tags={\"rm_cell", } \
  notebooks/sample.ipynb
```

#### Papermill