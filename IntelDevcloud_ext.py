import sys
import os
@cell_magic
def IntelDevcloud_Ext_Test(line, cell):
    with open(line, 'w') as f:
        for L in cell.split('\n'):
            f.write(L)
        os.system('chmod 755 q; chmod 755 run_kmeans_kernel.sh; if [ -x "$(command -v qsub)" ]; then ./q  run_kmeans_kernel.sh; else ./run_kmeans_kernel.sh; fi') 
    
def IntelDevcloud_Ext(line, cell):
    print(line)
    import sys
    i = 1
    for L in cell.split('\n'):
        print(i,L)
        i += 1
    print("--- END ---")
    
def load_ipython_extension(ipython):
    """This function is called when the extension is
    loaded. It accepts an IPython InteractiveShell
    instance. We can register the magic with the
    `register_magic_function` method of the shell
    instance."""
    ipython.register_magic_function(IntelDevcloud_Ext_Test, 'cell')
