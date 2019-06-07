for i in range(1, 16):
    with open(str(i) + '/README.md', 'a') as f:
        f.write('\n\n{% include lib/mathjax.html %}')
