# Build a Makefile

```
make

```

# Visualize the Tab and Blank

```
cat -e -t -v makefile_name.
```

It shows the presence of tabs with `^I` and line endings with `$`. Both are vital to ensure that dependencies end properly and tabs mark the action for the rules so that they are easily identifiable to the make utility.

