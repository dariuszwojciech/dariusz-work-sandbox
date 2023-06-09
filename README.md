# Purpose

#### WIP
I have 2 codebases that are of interest here: P and T - both for ADF json assets.

While it is possible to interact with ADF through its SDK (https://learn.microsoft.com/en-us/python/api/overview/azure/data-factory?view=azure-python), the purpose of this suite of tests is to test the assumptions of the work in progress.
You might compare it to static analysis of pipelines - as they are stored in json format before they get published.

Obviously, numbers/assumptions/assertions will need to be updated as we develop the pipelines.
At the moment, these tests will be to ensure we are aware of any changes we introduce to the code (also in ADF's low-code drag-and-drop) and that we eliminate of anything that is obsolete/dangling/unfinished.

## Development
Any python code will be (should be) reformatted using `black`.

## Assumptions
The required packages are in the `requirements.txt` file.
```
pip install -r requirements.txt
```

## Incubator folder
This folder contains the code that is not yet ready - highly experimental (sandbox) for experimentation and training purposes.

