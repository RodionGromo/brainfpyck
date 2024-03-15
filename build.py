import bfComp
import code2bf
import time

code2bf.compileFile(debug=False)
print("build complete!")
bfComp.runFile(debug=False)
