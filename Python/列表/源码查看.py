
# python函数源码查看
import inspect
import dill
inspect.getdoc(dill)
inspect.getsourcefile(dill)
inspect.getsourcelines(dill)

dill.source.getsourcelines(inspect)
dill.source.findsource(inspect) 
print(dill.source.findsource(min))