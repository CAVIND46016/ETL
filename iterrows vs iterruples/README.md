## Iterrows vs Itertuples
Inspired entirely by this blog:<br>
https://medium.com/swlh/why-pandas-itertuples-is-faster-than-iterrows-and-how-to-make-it-even-faster-bc50c0edd30d


### Output:
Creating dataframe...<br>
sum(val): 500000500000 | iterrows took 74.44801688194275 secs<br>
sum(val): 500000500000 | itertuples 1 took 0.5839943885803223 secs<br>
sum(val): 500000500000 | itertuples 2 took 0.5020027160644531 secs<br>
**sum(val): 500000500000 | itertuples 3 took 0.17999720573425293 secs**


### Conclusion:

<br>(i) Iterrows does a lot of type checks in the lifetime of its call, hence it's extremely slow.
<br>(ii) Itertuples are a lot faster due to the absence of these checks, and they can be tweaked to run quicker 
using the configuration: index=False & name=None.
