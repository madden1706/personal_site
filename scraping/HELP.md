There is an issue with the envs in VS Code.

Use:

```json 
{
    "python.venvPath": "~/anaconda3/envs/scraping/bin/python3",
    "python.pythonPath": "/Users/rossmadden/anaconda3/envs/scraping/bin/python3",
    "terminal.integrated.inheritEnv": false
}
```

in the "settings.json". It is something to do with the inheritance of the base env. 

More: https://github.com/microsoft/vscode-python/issues/5764

