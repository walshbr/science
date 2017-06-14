Assuming that your python file is named "newspaper_model.py" -

```
# start python
$ python

# import our file
import newspaper_model

# instantiate our Word2VecModel class in an instance called this_model
this_model = newspaper_model.Word2VecModel()

# access the .model attribute, which holds a fully vectorized corpus. Note that to run many of the word2vec commands you'll have to preface them with .wv. as the API has changed.
this_model.model.wv.similarity()
this_model.model.wv.vocab()
```
