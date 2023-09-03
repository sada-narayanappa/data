# Python Development Environments 

There are several ways to set up the python development environments:

* Just plain python environment installed on the machine
* Python Virtual Environment 
* Docker images 
* Kubernetes 

Each option has increasing amount of housekeeping and extra care but offers increased level of flexibility and large scale support. Not everyone needs the level of complexity. In the simplest case, virtual environment should do well for individual users. Using the *python* environment at the machine level is most easiest - I use that on my macbook although after this article I will change my practice.

I will explain each of the options in short summary. 

## Disadvantage of default python environment
This option is most easiest. Just install python on your system using [1] or 
[2]. Now, you can install the packages using pip or conda and use the system installation for all your development.

The ** advantage ** of this is you can develop without having any additional efforts other than to keep the system installation upto date.


The big ** disadvantage ** is that if you happen to need different version of library for testing or running some code, it can easily become a nightmare to keep the sanity together.

For example, here are some scenarios you can encounter that can make things messy

* If you download a LSTM package and it requires a different version of numy 3.4 but your application using numpy 3.7 and numpy 3.4 and 3.7 are incompatible. 

* Suppose you are reviewing and undrestanding some code published on github and it may have different package dependency than your local settings. You may be tempted to upgrade or downgrade your python installs which inturn may cause other copatibility issues. 

Enough said. Next immediate easiest way to avoid these conflicts are to use the virtual environment as described next.

## Virtual Environment

*(DO NOT USE virtualenv instead use vnev)*

virtual environment isolates different projects and manage dependencies.

### Install Python On Mac
> `brew install python@3.9` # OR `brew install python@3.8`
.
.
To list all installed python versions
	`brew list | grep python`
.
.
**OUTPUT**:  	
```
      148:python@3.10
      149:python@3.8
      150:python@3.9
```
.
Then you can use `python3.9`

#### Create virtual environment using venv

>\# create virtual environment
`python -m venv ~/venv/py39 `
\#
\# active by creating alias
\#
`source ~/venv/py39/bin/activate`
\# OR create alias in your .aliases
`alias py39='source ~/venv/py39/bin/activate'`
py39
\#
\# To deactivate type
`deactivate`

---
## References
[1] https://realpython.com/installing-python/#how-to-install-python-on-macos
[2] Anaconda https://www.anaconda.com/products/individual
[3] https://www.youtube.com/watch?v=N5vscPTWKOk‣
[4] https://www.youtube.com/watch?v=x9Hd2BmHt1o